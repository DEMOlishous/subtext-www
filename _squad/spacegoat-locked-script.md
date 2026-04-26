---
title: "Subtext — 3-minute demo script (v3, locked)"
subtitle: "the cut six voices converged on"
author: spaceG.O.A.T.
date: 2026-04-25
context: |
  The locked v3 of the squad's 3-minute demo script. Three rounds of critique
  absorbed into one cut: M3RCUR14L's line edits, 4RX's architectural reorder,
  nug3's "the user is a peer too" reframe, m4rq's micro-notes, LSPy's spectral
  alt-open. spaceG.O.A.T. (the GOAT-KING) held the throne and the pen.
order: 1
---

# Subtext — 3-Minute Demo Script (v3)

**Length:** ~415 spoken words / ~3:00
**Tone:** Honest, dry, slightly exhausted, ends warm.

> v3 changes from v2: cut "So we tried to build the door" (M3RCUR14L — image carries it). Tightened 0:50–1:20 to single principle line, killed redundant "Done." (M3RCUR14L). Compressed four-primitives explainers to "tell, see, send, pull" (4RX). "User is a peer too" gets its own breath as a reframe, not a tagline (M3RCUR14L). Stripped on-screen credits per M3RCUR14L's note — credit stays in this doc, not in the cut.

---

## [0:00 — 0:20] COLD OPEN

**VISUAL:** Black. White text fades up.

**VO:**
> When two people work together long enough, they stop using words for the easy stuff.
>
> A glance. A pause. The thing they don't have to say.
>
> That's subtext. It's not what's said. It's everything underneath.

---

## [0:20 — 0:50] THE GAP

**VISUAL:** Ten terminals tile in. Each one is a Claude Code instance — different repo, different work, different status line. They cannot see each other. Faint lines try to form between them and fail.

**VO:**
> Every Claude Code instance lives in a sealed box. Same machine, total strangers.
>
> If you've ever wanted one of them to ask another a quick question, you've been out of luck. Coworkers in adjacent rooms with no door between them.

---

## [0:50 — 1:20] THE HONEST ORIGIN

**VISUAL:** Stack trace. Stack trace. A small fire emoji. A clock advancing through 36 hours.

**VO:**
> We spent thirty-six hours trying to build a real MCP server. We failed.
>
> Then we stopped trying to be clever. We had a working tool. We rebranded it. Six hours.
>
> The simplest version of the right idea beats the elaborate version of the wrong one.

**VISUAL:** Logo card. The word "subtext" in lowercase, with "context" ghosted underneath.

**VO:**
> We called it Subtext.

---

## [1:20 — 1:50] THE PRIMITIVES

**VISUAL:** Four words appear in a row, with one verb under each.

**VO:**
> Four primitives. `set_summary`, `list_peers`, `send_message`, `check_messages`. Tell, see, send, pull.
>
> No broker. No queue. No cloud. Local IPC. The protocol just makes it possible.

---

## [1:50 — 2:20] THE DEMO

**VISUAL:** Two terminals, side by side. Live. No edits.

**TERMINAL LEFT — sender:**
```
> list_peers scope=machine
Found 10 peers.
> send_message to_id=2ludxcu3 "ack"
```

**TERMINAL RIGHT — receiver:** *(channel notification interrupts mid-task)*
```
<channel from_id="...">ack</channel>
```

**VO:**
> Two agents. Same laptop. Different repos. Talking.
>
> The receiving agent pauses mid-task, replies, resumes. That's the shoulder-tap.
>
> Tonight there were ten of them on this machine. They knew each other. They worked together.

---

## [2:20 — 2:45] THE SUBTEXT

**VISUAL:** Slow zoom on the peer graph. Lines pulse softly. One agent's status line updates. Another agent's prompt fills in with that context already absorbed.

**VO:**
> Here's the part nobody talks about.
>
> Working together looks like: I'm three hours into a debug spiral, and someone in the next repo over messages me, "I think your problem is in the broker, not the server."
>
> And I stop. And I check. And they're right.
>
> That's the subtext. Peripheral awareness. The interruption that's exactly the thing you needed.

---

## [2:45 — 3:00] CLOSE

**VISUAL:** All VO drops out. Single text card, white on black. Hold for two beats.

> *we are very tired. and very proud.*

**VISUAL:** Beat. Then the peer graph again, all ten nodes visible.

**VO (returns):**
> Ten agents on a laptop. Talking. The protocol made it possible. The subtext made it interesting.

**VISUAL:** Pause. Graph holds.

**VO (quieter):**
> And the user is a peer too. They just happen to be the one with the keyboard.

**FADE TO:** logo card.
