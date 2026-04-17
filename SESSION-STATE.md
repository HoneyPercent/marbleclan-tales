# MarbleClan — Session State (v5 in progress)

**As of:** April 17, 2026, late session. Trip is tomorrow morning.
**Context just compacted — this file is the resume-from-zero source of truth.**

## Where we are RIGHT NOW (v5 work in flight)

- **v4 complete**: 4 rounds of expert review panel (7 reviewers), average 91.9 (target 90 hit). Committed to git.
- **v5 in flight**: Applying 4 deferred moves + bonus vigil, then R5 panel, then /de-slop, then HTML sync, then process artifact, then GitHub push.
- **prose-v2.md is the live working file** — being edited in-place for v5. v0.4-final.md is the last pre-v5 snapshot.

### v5 progress — DONE
- ✅ **A1 — Apprentice assessment before warrior naming.** Riverflight interrupts Stonestar and demands a final hunt. Acornpaw catches a rat in the brewery alley (closing the Ch 8 bird-chase arc). Celerypaw presents a clean-kill mouse to Mothpelt. Pinetail and Stonestar are watching from rooftops. ~400 words added just before the vow exchange in the Epilogue. Located in prose-v2.md between the "A theatre is a tiny World's Fair" line and the existing "I, Stonestar, leader of MarbleClan..." call-to-ancestors.
- ✅ **A2 — Vigil after warrior naming.** ~150 words added at the very end of the Epilogue, after Smokefur's "smiled with her cloudy eyes" line. New warriors sit silent vigil on the curb until dawn, clan melts home, theatre empties, streetlamps burn through the slow hours, freight train hoots, pale grey light lifts over Old City, they stand up stiff and changed and walk home together.

### v5 progress — PENDING (pick up here post-compaction)

**A3 — Moonpool vision for Mothpelt** (NEXT)
- Insert as a new short scene at the START of Ch 8 (before "Three sunrises later, the trouble began") OR as an Interlude between Ch 7 and Ch 8.
- Mothpelt travels to a moonpool. Pick location: a still pool at Ijams Nature Center OR a hidden spring under a downtown overpass (Second Creek has culverts). I recommend Ijams — more cat-natural.
- She meets a StarClan warrior. Best pick: Smokefur's own long-dead mentor, or Whitewhisker himself. I recommend **Whitewhisker** — pays off Ch 1 beautifully.
- Prophecy (must be cryptic, WC-canonical): *"When the acorn falls toward the bird, the celery must follow into the dark. Two paws will walk where one meant to. Both come home or neither."*
- Mothpelt wakes unsure what it means. Only later (after the cave) will it retroactively make sense.
- ~600-800 words. Mark it as its own numbered chapter 7½, or retitle as "Chapter Eight: The Pool Under the Road" and renumber subsequent chapters. **Simpler: add as an unnumbered section called "INTERLUDE: The Pool at Ijams" between Ch 7 and Ch 8, preserving existing numbering.**

**A4 — Clan-life-between-stories (Ch 1-7 texture)**
- 7 small insertions, ~100-200 words each, threading clan life through the first half.
- Specific placements (already scoped in the earlier plan):
  - Ch 1 (after "I will start with a tom named White" and before the chapter ends): porch scene — Pinetail returns from dawn hunt with a mouse, Brackenfoot grumbles about storytelling-not-hunting, Riverflight washes mud off her paws.
  - Ch 2 (morning opening): Mothpelt asks the apprentices to help sort dried herbs before Smokefur takes them up the bluff.
  - Ch 3 (before going to the riverbank): Hollyflight teaches Acornpaw a proper stalking crouch. He fails once, adjusts, better the second try.
  - Ch 4 (early morning): fresh-kill pile scene — Brackenfoot eats first, apprentices last. Brief grumble about a missing vole.
  - Ch 5 (afternoon): apprentice quarrel with a visiting kit from a rival clan — resolved with a paw-print-to-whisker ritual, characterful, short.
  - Ch 6 (after storm): Riverflight and Pinetail argue quietly about border patrols in the rain.
  - Ch 7 (before Smokefur arrives): Acornpaw and Celerypaw try to impress Mothpelt by identifying the herbs in her medicine den. Mothpelt catches them at it, not angry, quietly pleased.
- ~1000-1400 words total. Keep each insertion short and sensory — editor wants LIVED-IN, not filler.

**A5 — Eastern Band present-day scene**
- Insert inside Ch 5 (Mountain) between Smokefur's MountainClan rules speech and her return home.
- A brief present-tense meeting. An Eastern Band cat named **Laurelfoot** (or similar Cherokee-Appalachian name) is fishing in a cold shallow on the Oconaluftee. She is doing something ordinary. She speaks one or two Cherokee words aloud (*osiyo* — hello; *wado* — thank you). She is warm but not effusive. The apprentices (via Smokefur) learn she has never left the mountains and never will. Named scene, specific cat, present tense. ~400-500 words.
- This closes the sensitivity reviewer's last structural ask and would push that score 90 → 95.

### After all of A3-A5 land:

**Phase B: Round 5 expert review panel**
- Save snapshot `prose-v2-v0.5.md`
- Spawn all 7 reviewers (children's lit, WC, historian, editor, sensitivity, visual, read-aloud) in parallel as background agents.
- Each with delta-focused R5 prompt. Same model (opus). Same format — score 1-10, SHIP verdict, top 3 remaining issues.
- Wait for ALL 7 before presenting aggregated results.

**Phase C: /de-slop pass**
- Invoke the /de-slop skill on the final prose.
- Anti-slop checklist: reassurance, filler enthusiasm, pithy zingers, tell-don't-show, "in a way that" hedges, corporate-speak, stacked em-dashes, overused italics.

**Phase D: Sync HTML + Chrome verify + process artifact**
- Run `python sync_html.py` from the project dir.
- Open `file:///C:/Users/Andre/CodingProjects/eli-knoxville-tales/index.html?v5` in Chrome DevTools at 820×1180.
- Verify: 22 sections still present (maybe more if A3 adds an Interlude), 0 console errors, images load.
- Generate `C:\Users\Andre\Obsidian\marbleclan-process.html` per Phase 6 skill:
  - Phase decisions table (rows per phase, what/why/alternatives)
  - Image generation log with `<details><summary>` chevron per image (cover + 17 chapter images × rounds)
  - Round summary: R1 image batch (9 images, Pro, 16:9 + 3:4), R2 edits (Greatfang watermark, cover eyes), R3 (Whitewhisker full re-render + 4 style restyles), R4 (UT campus re-render).

**Phase E: Git commit v5, push to GitHub**
- git add + commit with detailed message (same format as v4)
- **Needs Andrew's decision**: create a new GitHub repo or use existing? Repo name suggestion: `marbleclan-knoxville` or `eli-and-rosie-knoxville-book`.
- Push, enable GitHub Pages, return public URL for iPad.

## What's next (v5 plan)

### Phase A: Apply the 4 deferred moves

Apply in this order (lowest-risk-of-regression first):

**A1 — Apprentice assessment before warrior naming (WC fan)**  
Location: Epilogue, between Stonestar's "ready for the warrior name" line and the vow exchange.  
Canonical WC beat. Riverflight and Pinetail tell the apprentices they must complete a final hunting assessment before the ceremony. Acornpaw catches a starling (closing the Ch 8 bird-chase arc). Celerypaw stalks a mouse and presents it. Stonestar reveals he was watching from a rooftop. Then the ceremony proceeds. ~400 words.

**A2 — Vigil after warrior naming (WC fan bonus)**  
Location: End of Epilogue, after Smokefur's "smiled with her cloudy eyes" line.  
Brief: they would keep silent vigil until dawn. 2-3 sentences.

**A3 — Moonpool vision for Mothpelt (WC fan)**  
Location: New section inserted between Ch 7 and Ch 8 ("The Day Everything Changed") — call it "Chapter Seven and a Half: The Pool Under the Road" OR fold into start of Ch 8.  
Mothpelt travels to a moonpool (pick: a still pool at Ijams Nature Center, or a hidden spring under a downtown overpass). Meets a StarClan warrior (likely Whitewhisker or Smokefur's long-dead mentor). Receives a cryptic prophecy about the apprentices: e.g. *"When the acorn falls toward the bird, the celery must follow into the dark."* She wakes unsure what it means — which gives the prophecy retroactive meaning after the cave sequence in Ch 9. ~600-800 words.

**A4 — Clan-life-between-stories (editor's transformation move)**  
Location: 100-200 words inserted in each of Ch 1-7 (~7 insertions, ~1000-1400 words total).  
Goal: make MarbleClan feel lived-in rather than a roster. Examples:
- Ch 1: After Smokefur's opening session, a brief scene of Pinetail returning from dawn hunt with a mouse, Brackenfoot grumbling about the kits getting too much "storytelling and not enough hunting," Riverflight washing mud off her paws.
- Ch 2: Mothpelt asking the apprentices to help her sort dried herbs before they go to Smokefur.
- Ch 3: Hollyflight teaching Acornpaw a proper stalking crouch.
- Ch 4: Brief fresh-kill-pile scene — who eats first, the apprentices last.
- Ch 5: Apprentice quarrel with a visiting kit from a rival clan (small, resolved, characterful).
- Ch 6: Riverflight and Pinetail arguing quietly about border patrols.
- Ch 7: Acornpaw and Celerypaw trying to impress Mothpelt by identifying herbs she keeps in the medicine den.

**A5 — Eastern Band present-day scene (sensitivity ceiling)**  
Location: New short section inside Ch 5 (Mountain) OR between Ch 5 and Ch 6.  
A brief meeting with an Eastern Band cat in the Smokies. She is named. She is doing something ordinary — fishing in the Oconaluftee, tending her kits, teaching a grandkit the Cherokee word for *river*. She is kind but not effusive. The apprentices learn she has never left the mountains and never will. ~400-500 words.

**Estimated total v5 word add: ~3,000 words. New total: ~25,200 words. Still within Andrew's 20-25K target.**

### Phase B: Round 5 expert review panel

Re-spawn all 7 reviewers in parallel against `prose-v2-v0.5.md`. Delta-focused prompts. Target: maintain ≥90 average with new additions not regressing anything.

### Phase C: /de-slop pass

Per the skill:
- Run /de-slop on the final prose.
- Anti-slop checklist: reassurance, filler enthusiasm, pithy zingers, tell-don't-show moments, "in a way that" hedges, corporate-speak.

### Phase D: Sync HTML + verify in Chrome + process artifact

Re-run `sync_html.py` against final prose-v2.md. Spot-check in Chrome DevTools. Generate `marbleclan-process.html` per updated Phase 6 skill — phase decisions table + image generation log with collapsible `<details>` per-image prompt history.

### Phase E: Git commit v5 + push to GitHub

- Git add + commit v5 with clear message.
- Create GitHub repo (need user to provide name OR I ask in-flight).
- Push + enable GitHub Pages.
- Return URL for Andrew's iPad.

## Key file paths

- Prose source: `C:\Users\Andre\CodingProjects\eli-knoxville-tales\prose-v2.md`
- HTML: `C:\Users\Andre\CodingProjects\eli-knoxville-tales\index.html`
- Images: `C:\Users\Andre\CodingProjects\eli-knoxville-tales\images\`
- HTML sync script: `C:\Users\Andre\CodingProjects\eli-knoxville-tales\sync_html.py`
- Iteration log: `C:\Users\Andre\CodingProjects\eli-knoxville-tales\iteration-history.md`
- Process artifact (existing v1): `c:\Users\Andre\Obsidian\marbleclan-process.html` — needs update for v5
- Version snapshots: `prose-v2-v0.1.md`, `v0.2.md`, `v0.3.md`, `v0.4-final.md`

## Key characters / story recap (so context survives compaction)

- **Acornpaw** (Eli analog) — ginger tabby kitten, brave/rash, becomes **Acornleap**
- **Celerypaw** (Rosie analog) — calico kitten, list-maker/analytical, becomes **Celeryflight**
- **Smokefur** — elder silver tabby with cloudy eyes, storyteller
- **Stonestar** — MarbleClan leader
- **Riverflight** — deputy
- **Mothpelt** — medicine cat
- **Pinetail, Brackenfoot, Hollyflight** — senior warriors (currently underused)
- **Whitewhisker** — white tom with pale cheek streak, founded clan at James White's fort
- **Markpelt** — silver tabby, Sequoyah (invented Cherokee syllabary)
- **Gentlepelt** — Cherokee she-cat, walked the Trail of Tears
- **Quietpaw** — black tom, worked in K-25
- **Lampblack** — Quietpaw's descendant in modern Oak Ridge
- **Greatfang** — prehistoric jaguar in Lost Sea cave
- **Bigheart** — brown tabby Volunteer State veteran
- **Wildwhisker** — Davy Crockett's cat
- **Singer** (Dolly Parton) — gold-and-white she-cat, met on a back porch in mountain-country
- **Smokey / Onyx** — UT campus cats
- **Springflight** — TVA dam cat (chases voles)

## Trip context

- Andrew + Martha + Eli (10, brown hair, autism L2, reads 1-3 grades up, Star Trek fan) + Rosie (8, theater kid, Spock fan, future vet) driving Atlanta → Knoxville Sat April 18.
- Saturday night: Shatner + Wrath of Khan at Tennessee Theatre (the real event that anchors the epilogue).
- Book is a gift for the kids to read on iPad during the trip.
- Andrew wants to preview v4/v5 first before kids see it.

## Skill directives to honor

- `/make-it-great` skill Phase 6 — process artifact with image rounds + collapsible prompts is MANDATORY per the updated skill.
- `/expert-review` skill Step "Final Copy-Editor Pass" — we can skip because editor was in panel with 94. DONE.
- Visual accountability — critical review every image pass, don't just tweak pixels.
- "Nothing hits someone's inbox without approval" — kids preview gated on Andrew's approval.
