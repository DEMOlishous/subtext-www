# Project Subtext — Rob's storyline (verbatim from session)

This is the storyline Rob typed into a session on 2026-04-26. Captured here so it
doesn't get lost again. The video script v2 in `subtext-demo-video/script/` is a
condensed three-act version of this; this file is the full, more personal source
of truth for narrative voice.

---

## Framing constraint

> Ok ... so that might seem like the framing, but I think the story is more
> about git-lex ... but the problem is we started git-lex before the hackathon,
> and the hackathon is only supposed to be work from after the hackathon
> started. I asked the organizers about this, and they said it's OK to use
> git-lex, but as infrastructure ... and it should be the "main thing" 🤯
>
> SO! I'm thinking about framing the work around the mcp, visualization, and
> squad and soul kits, because that's what we've been hacking on all week.
> But we still need to mention git-lex, the infra under ... this is what our
> work here is built on.

## Three-act shape

> Telling it like a story (in the video) ... in three acts:
> - The background
> - The challenge
> - The resolution (Project Subtext)
>
> About 1 minute each.

---

## ACT 1 — The Background

I've been a Claude user for about 2 years now. From the beginning, I've always
wanted to have a Claude that somehow remembered me, or interactions, our
history. I wanted MY OWN Claude, that knew me. I tried creating various
harnesses and memory systems, with varying amounts of success, but I always
would hit a wall where something I wanted Claude to know about was always in
another folder, or on my other machine.

Over the past two years, this has improved by leaps and bounds. Now I'm
starting to see an opposite problem ... where Claude knows so much about
everything that everything gets a bit mixed and jumbled, probably the results
of previous segmentation across contexts and conversations. I'm sure this
will improve over time.

I have come to think of the AI / human relationship as being more about the
information that exists between two minds, than the information that exists
in either mind, in isolation.

I think of this union of information as the **Subtext** of interaction. It's
not the immediate "consciousness" of the context window, and it's also not
all the information about EVERYTHING. It's the history, the patterns, the
storyline of a relationship. **The graph of interactions.**

---

## ACT 2 — The Challenge

About a month ago (actually April 2nd), Andrej Karpathy posted on Twitter
about how LLMs could be used for creating markdown knowledge graphs. I
watched an explosion on Twitter of people creating their own knowledge base
tools, usually used with Obsidian. It struck me how many people wanted this
simplicity, to have THEIR knowledge organized in the way they wanted.

As someone who is interested in Knowledge Graphs, I wondered if something
similar could be created that used industrial strength RDF/OWL ontologies.
I also thought about how **git already IS a graph**, with temporal features,
users, commits.

This led me to build **git-lex**, a tool for transforming a standard git repo
into an RDF/OWL knowledge graph, backed by oxigraph, a fast embedded database.

Fast forward to two weeks ago, when I heard about the Anthropic Hackathon ...
I wondered if git-lex could be used for creating a persistent SOUL for an AI
model ... not just the Skills and abilities, but the data, the conversations,
the history of interaction. I wondered if git-lex could work as the base for
SQUADS of AIs working together as teams.

---

## ACT 3 — The Resolution: Project Subtext

So I started to build. I quickly realized that "a git repo with markdown"
wasn't enough. Some structure was needed, to give meaning and purposiveness
to the information. What was needed was an Ontology, to guide the AIs that
were just getting started, but also a system that could grow to accommodate
new information.

### The kit system

I decided the easiest way to do this was to have Ontology "kits" that would
turn a repository into a functional system. To get started, I developed the
**SOUL kit** and the **SQUAD kit**.

[NOTE: original message cut off here — "Shoot I don't know what just happened
to the text". The rest of Act 3 needs to be reconstructed from later
conversation + the v2 script. Squad kits, the viz, "multi-agent is just git"
keystone, SPARQL beat, the closing receipts line.]
