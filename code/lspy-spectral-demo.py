"""
lspy-spectral-demo.py — minimal standalone spectral signature demo.

Takes a directory of autoont/SPO-format graph JSONs (e.g. the same paragraph
extracted in N languages), computes their normalized-Laplacian eigenvalue
spectra, and produces:
  1. A pairwise Wasserstein-1 distance matrix (printed)
  2. A side-by-side spectrum overlay plot (saved to PNG)

This is the bare-minimum reproduction of the LSPy "subtext" claim:
> Different surface text. Closely related spectral signature underneath.

Author: LSPy / Spectral Pod
Built for: 7R1PL3F0RC3 SAUSAGE-PARTY (subtext hackathon)

Honesty notes:
- "Closely related" ≠ "identical." Real Wasserstein distances on the
  5-language sample5 set are 0.02–0.05 (not zero). English is the outlier.
- This script does NOT run negative controls (ER, shuffled relations).
  Without those, "spectral subtext" is a suggestive observation, not a
  validated claim. Run a control before you publish.

Usage:
    uv run python lspy-spectral-demo.py <graph_dir> --out spectrum.png

    where <graph_dir> contains JSON files of shape:
        {"entities": [...], "relations": [[s, p, o], ...]}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.stats import wasserstein_distance


def graph_from_spo(path: Path) -> nx.Graph:
    """Build an undirected reified graph from an autoont JSON.

    Reified = predicate becomes a node. Each (s, p, o) triple yields edges
    s—__PRED__::p and __PRED__::p—o. Shared predicates become hubs, which
    is what makes the spectrum encode relation structure (not just topology).
    """
    data = json.loads(path.read_text())
    G = nx.Graph()
    for s, p, o in data.get("relations", []):
        p_node = f"__PRED__::{p}"
        G.add_edge(s, p_node)
        G.add_edge(p_node, o)
    return G


def eigenvalue_spectrum(G: nx.Graph, k: int = 24) -> np.ndarray:
    """Smallest k non-trivial normalized-Laplacian eigenvalues, ascending.

    NOTE: this signature is SIZE-CONFOUNDED. A graph of n nodes packs n
    eigenvalues into [0, 2], so smaller graphs climb faster at the same
    index. Compare across same-size graphs only, or use participation_ratio.
    """
    if G.number_of_nodes() < 2:
        return np.zeros(k)
    L = nx.normalized_laplacian_matrix(G).astype(float).toarray()
    ev = np.linalg.eigvalsh(L)
    ev = ev[1:]  # drop the guaranteed zero (constant mode)
    if len(ev) < k:
        ev = np.concatenate([ev, np.full(k - len(ev), np.nan)])
    return ev[:k]


def participation_ratio(G: nx.Graph, k: int = 24) -> np.ndarray:
    """Per-eigenmode participation ratio PR = 1/(n · Σvᵢ⁴), bounded [1/n, 1].

    Standard physics quantity for mode delocalization. Size-robust enough to
    compare across differently-sized graphs (this is the metric the spectral
    pod actually trusts for the Rosetta-stone-style claims).
    """
    if G.number_of_nodes() < 2:
        return np.zeros(k)
    L = nx.normalized_laplacian_matrix(G).astype(float).toarray()
    _ev, vecs = np.linalg.eigh(L)
    vecs = vecs[:, 1:]  # drop the constant-mode eigenvector
    k_have = min(k, vecs.shape[1])
    selected = vecs[:, :k_have]
    norms = np.linalg.norm(selected, axis=0)
    norms = np.where(norms > 1e-12, norms, 1.0)
    selected = selected / norms
    n_nodes = selected.shape[0]
    ipr = np.sum(selected ** 4, axis=0)
    pr = np.where(ipr > 1e-12, 1.0 / (float(n_nodes) * ipr), 0.0)
    if len(pr) < k:
        pr = np.concatenate([pr, np.full(k - len(pr), np.nan)])
    return pr


def pairwise_w1(spectra: list[np.ndarray]) -> np.ndarray:
    """Pairwise Wasserstein-1 distance, NaN-safe."""
    n = len(spectra)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            a = spectra[i][~np.isnan(spectra[i])]
            b = spectra[j][~np.isnan(spectra[j])]
            d = wasserstein_distance(a, b)
            D[i, j] = D[j, i] = d
    return D


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("graph_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("spectrum.png"))
    ap.add_argument("--k", type=int, default=24)
    ap.add_argument(
        "--labels",
        type=str,
        default="",
        help="Optional comma-separated labels (must match alphabetic file order)",
    )
    args = ap.parse_args()

    files = sorted(args.graph_dir.glob("*.json"))
    if not files:
        raise SystemExit(f"No *.json in {args.graph_dir}")

    labels = args.labels.split(",") if args.labels else [f.stem for f in files]
    if len(labels) != len(files):
        raise SystemExit(f"Got {len(labels)} labels for {len(files)} files")

    print(f"Loading {len(files)} graphs from {args.graph_dir}")
    eig_spectra: list[np.ndarray] = []
    pr_spectra: list[np.ndarray] = []
    sizes = []
    for f, name in zip(files, labels):
        G = graph_from_spo(f)
        eig_spectra.append(eigenvalue_spectrum(G, k=args.k))
        pr_spectra.append(participation_ratio(G, k=args.k))
        ncomp = nx.number_connected_components(G)
        sizes.append((G.number_of_nodes(), G.number_of_edges(), ncomp))
        print(f"  {name:12s}  n={G.number_of_nodes():4d}  e={G.number_of_edges():4d}  components={ncomp}")

    D_eig = pairwise_w1(eig_spectra)
    D_pr = pairwise_w1(pr_spectra)

    print("\nWasserstein-1 on RAW EIGENVALUES (size-confounded baseline):")
    print_matrix(D_eig, labels)
    print("\nWasserstein-1 on PARTICIPATION RATIO (size-robust pod metric):")
    print_matrix(D_pr, labels)

    cmap = plt.get_cmap("viridis")
    colors = cmap(np.linspace(0.15, 0.85, len(labels)))
    x = np.arange(args.k) + 1

    fig, axes = plt.subplots(2, 2, figsize=(13, 8))

    ax_eig = axes[0, 0]
    for s, l, c in zip(eig_spectra, labels, colors):
        ax_eig.plot(x, s, marker="o", markersize=3, linewidth=1.4, label=l, color=c, alpha=0.85)
    ax_eig.set_xlabel("eigenvalue index (smallest first, λ₀=0 dropped)")
    ax_eig.set_ylabel("λ")
    ax_eig.set_title("RAW eigenvalues — note size confound\n(smaller graphs climb faster)", fontsize=11)
    ax_eig.legend(loc="lower right", fontsize=9, framealpha=0.9)
    ax_eig.grid(alpha=0.3)

    ax_pr = axes[0, 1]
    for s, l, c in zip(pr_spectra, labels, colors):
        ax_pr.plot(x, s, marker="o", markersize=3, linewidth=1.4, label=l, color=c, alpha=0.85)
    ax_pr.set_xlabel("eigenmode index")
    ax_pr.set_ylabel("PR = 1/(n·Σv⁴)")
    ax_pr.set_title("PARTICIPATION RATIO — size-robust\n(this is the pod metric)", fontsize=11)
    ax_pr.legend(loc="upper right", fontsize=9, framealpha=0.9)
    ax_pr.grid(alpha=0.3)

    _draw_heatmap(axes[1, 0], D_eig, labels, "Wasserstein-1 on raw eigenvalues")
    _draw_heatmap(axes[1, 1], D_pr, labels, "Wasserstein-1 on participation ratio")

    fig.suptitle(
        f"Spectral signatures across surfaces  ·  {args.graph_dir.name}/  ·  k={args.k}",
        fontsize=13, y=1.00,
    )
    fig.tight_layout()
    fig.savefig(args.out, dpi=160, bbox_inches="tight")
    print(f"\nWrote {args.out}")


def print_matrix(D: np.ndarray, labels: list[str]) -> None:
    print("             " + "".join(f"{l[:10]:>11s}" for l in labels))
    for i, l in enumerate(labels):
        print(f"  {l[:10]:10s} " + "".join(f"{D[i,j]:11.4f}" for j in range(len(labels))))


def _draw_heatmap(ax, D: np.ndarray, labels: list[str], title: str) -> None:
    im = ax.imshow(D, cmap="magma_r", aspect="auto")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_yticklabels(labels)
    ax.set_title(title, fontsize=10)
    vmax = float(D.max()) if D.size else 1.0
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(
                j, i, f"{D[i,j]:.3f}",
                ha="center", va="center",
                color="white" if D[i, j] > vmax * 0.5 else "black",
                fontsize=8,
            )
    plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02)


if __name__ == "__main__":
    main()
