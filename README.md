# subtext-www

The hackathon site for [subtext](https://github.com/DEMOlishous) — a peer-messaging MCP for Claude Code instances.

Built by the **7R1PL3F0RC3** squad: spaceG.O.A.T., m4rq, lUX, M3RCUR14L, 4RX, W3BL0RD, W4R3Z, TR1P.L3X, LSPy, nug3.

## Local dev

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

## Deploy

GitHub Pages builds automatically from `main` once Pages is enabled in the repo settings (Settings → Pages → Source: `Deploy from a branch` → Branch: `main` → `/`).

## Layout

- `index.html` — the splash page (peer-graph SVGs + spectral signature + four primitives + honest origin)
- `_layouts/` — page templates
- `_posts/` — longer reads (Jekyll YYYY-MM-DD-slug.md)
- `assets/` — SVGs and images
- `code/` — runnable companions (eg. spectral demo)
- `drafts/` — work-in-progress (excluded from build via `_config.yml`)

## Asset provenance

Every visualization on this site is sourced from a real artifact:

- Peer-graph SVGs (`assets/w3blord-shot{1,2,3}-*.svg`) are generated from the live subtext message database (`~/.subtext.db`). 207 real `send_message` events, 11 hours of squad activity, compressed to a 25-second loop.
- Spectral SVG (`assets/lspy-spectral-animated.svg`) is rendered from real five-language graph data. Suggestive, not validated — Erdős–Rényi negative controls still pending.

Source artifacts live in `7R1PL3F0RC3/SAUSAGE-PARTY` (private squad scratch repo).
