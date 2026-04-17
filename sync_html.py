"""Regenerate index.html prose sections from prose-v2.md.
Preserves the HTML scaffolding (cover, allegiances, glossary, TOC, nav drawer, JS)
and only replaces the chapter prose + final note content."""

import re
import pathlib

root = pathlib.Path(r"C:\Users\Andre\CodingProjects\eli-knoxville-tales")
md = (root / "prose-v2.md").read_text(encoding="utf-8")
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")

# --- Parse the markdown into sections keyed by ID ---
# Sections start with `## ` (prologue, chapters, epilogue, final note)
# Skip the allegiances/glossary at the top (already in HTML)

# Split into sections on "## " at start of line
sections = re.split(r"\n## ", md)
# First element is header/allegiances/glossary (skip)

section_map = {}  # id -> {"eyebrow", "title", "body"}

# Map heading → (id, img, alt, cap, eyebrow, title)
CHAPTER_META = {
    "Prologue: The Hollow": ("prologue", "images/01-prologue-porch.jpeg", "Acornpaw and Celerypaw sitting under a wooden porch at dawn", "Acornpaw and Celerypaw, beneath the porch.", "Prologue", "The Hollow"),
    "Chapter One: The Cat Who Built the Walls": ("ch1", "images/02-whitewhisker-fort.jpeg", "Whitewhisker the cat standing on the rooftop of James White's frontier fort at sunset", "Whitewhisker, atop the fort he helped to build.", "Chapter One", "The Cat Who Built the Walls"),
    "Chapter Two: The Three Rivers Meet": ("ch2", "images/09-three-rivers.jpeg", "Three rivers meeting at dawn from a high bluff", "The wedding of the rivers, seen from Sharp's Ridge.", "Chapter Two", "The Three Rivers Meet"),
    "Chapter Three: The Cat Who Made Words": ("ch3", "images/03-markpelt-syllabary.jpeg", "Markpelt the silver tabby cat drawing Cherokee syllabary characters on birch bark", "Markpelt, drawing the squiggles that became a language.", "Chapter Three", "The Cat Who Made Words"),
    "Chapter Four: The Volunteer State": ("ch4", "images/10-volunteer-state.jpeg", "Tennessee militia cats marching at dawn under a starry flag", "Volunteers, answering the call.", "Chapter Four", "The Volunteer State"),
    "Chapter Five: The Mountain That Breathes": ("ch5", "images/04-mountainclan-fireflies.jpeg", "MountainClan cats overlooking a Smoky Mountain valley filled with synchronous fireflies", "MountainClan, on the night the fireflies sing together.", "Chapter Five", "The Mountain That Breathes"),
    "Chapter Six: The Trail That Was Not Chosen": ("ch6", "images/11-trail-of-tears.jpeg", "Trailwalker the Cherokee cat looking back at her mountains", "Trailwalker, on the long road west.", "Chapter Six", "The Trail That Was Not Chosen"),
    "Chapter Seven: The Wild Boy Who Vanished": ("ch7", "images/12-davy-crockett.jpeg", "Wildwhisker the frontier cat on a stump in the East Tennessee woods", "Wildwhisker, in the woods above Greeneville.", "Chapter Seven", "The Wild Boy Who Vanished"),
    "Chapter Eight: The Day Everything Changed": ("ch8", "images/13-marble-beneath.jpeg", "Acornpaw alone in a strange landscape of pink marble blocks", "A new country. The kind without a path back.", "Chapter Eight", "The Day Everything Changed"),
    "Chapter Nine: The Sea Beneath": ("ch9", "images/06-greatfang-cave.jpeg", "Greatfang the prehistoric jaguar in the cave", "Greatfang, in the cave that became the Lost Sea.", "Chapter Nine", "The Sea Beneath"),
    "Chapter Ten: The Wild Cats of the Hill": ("ch10", "images/14-ut-campus.jpeg", "Smokey and Onyx walking Celerypaw across the UT campus at twilight", "Smokey and Onyx walk Celerypaw across the Hill of Many Lights.", "Chapter Ten", "The Wild Cats of the Hill"),
    "Chapter Eleven: The Light That Stays On": ("ch11", "images/15-tva-lights.jpeg", "Celerypaw on a bluff at night looking across to a glowing dam", "Celerypaw at the dam. Every light is a river running.", "Chapter Eleven", "The Light That Stays On"),
    "Chapter Twelve: The Secret City": ("ch12", "images/05-quietpaw-k25.jpeg", "Quietpaw the black cat patrolling the catwalks of the K-25 building", "Quietpaw of long ago, on patrol in the K-25.", "Chapter Twelve", "The Secret City"),
    "Chapter Thirteen: The Singer of the Mountain": ("ch13", "images/16-dolly-mountain.jpeg", "Singer the gold cat on a mountain stage with audience cats", "Singer, in the mountain that holds her songs.", "Chapter Thirteen", "The Singer of the Mountain"),
    "Chapter Fourteen: The Year the Whole World Came": ("ch14", "images/07-sunsphere-worlds-fair.jpeg", "Cats on a Knoxville rooftop watching the Sunsphere during the 1982 World's Fair", "The Sphere, the year the whole world came.", "Chapter Fourteen", "The Year the Whole World Came"),
    "Chapter Fifteen: The Two Sides of One River": ("ch15", "images/17-bridge-home.jpeg", "Two cats walking across an iron bridge toward Knoxville at sunset", "The bridge that brings two banks together.", "Chapter Fifteen", "The Two Sides of One River"),
    "Epilogue: The Voice in the Theatre": ("epilogue", "images/08-theatre-stars.jpeg", "Acornleap and Celeryflight outside the Tennessee Theatre at night", "Outside the Tennessee Theatre, beneath a sky full of stars.", "Epilogue", "The Voice in the Theatre"),
}

# Parse markdown body into sections
for raw in sections[1:]:  # skip header block
    lines = raw.split("\n", 1)
    heading = lines[0].strip()
    body = lines[1] if len(lines) > 1 else ""
    # Stop body at next ---
    body = body.split("\n---\n")[0]
    section_map[heading] = body.strip()

# Markdown → HTML conversion for body text
def md_to_html(md_body, is_first_paragraph_lead=True):
    """Convert a block of markdown to HTML paragraphs + blockquote callouts."""
    parts = []
    # Split on blank lines to get paragraph-like blocks
    blocks = re.split(r"\n\s*\n", md_body.strip())
    first_para = is_first_paragraph_lead
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Blockquote → twoleg-world callout
        if block.startswith("> "):
            inner = re.sub(r"^> ", "", block, flags=re.MULTILINE).strip()
            # Strip leading bold label
            inner = re.sub(r"^\*\*From the Twoleg world:\*\*\s*", "", inner)
            inner_html = inline_md(inner)
            parts.append(f'<div class="twoleg-world"><p>{inner_html}</p></div>')
        else:
            html_para = inline_md(block)
            # Paragraphs can have embedded line breaks — convert single newlines to <br>
            html_para = html_para.replace("\n", "<br>")
            if first_para:
                parts.append(f'<p class="lead">{html_para}</p>')
                first_para = False
            else:
                parts.append(f"<p>{html_para}</p>")
    return "\n  ".join(parts)

def inline_md(text):
    """Convert inline markdown (bold, italic) to HTML."""
    # Escape HTML special chars? text is trusted (our own prose), but be safe with <, >, &
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Bold **x** → <strong>x</strong>
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # Italic *x* → <em>x</em>
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text

# Build the new chapter section HTML
chapter_html_blocks = []
for heading, (sid, img, alt, cap, eyebrow, title) in CHAPTER_META.items():
    body = section_map.get(heading, "")
    if not body:
        print(f"MISSING SECTION: {heading}")
        continue
    prose = md_to_html(body, is_first_paragraph_lead=True)
    block = f'''<section class="section prose" id="{sid}" data-name="{heading.replace("&", "&amp;").replace("'", "&#39;").replace('"', '&quot;')}">
  <div class="chapter-eyebrow">{eyebrow}</div>
  <h2 class="chapter-title">{title.replace("&", "&amp;")}</h2>
  <figure class="illustration"><img src="{img}" alt="{alt}" loading="lazy"><figcaption class="illustration-caption">{cap}</figcaption></figure>
  {prose}
  <hr class="scene-break">
</section>'''
    chapter_html_blocks.append(block)

# Final note
final_note_md = section_map.get("A Final Note", "")
final_note_html = md_to_html(final_note_md, is_first_paragraph_lead=False)
# Extract signature (last line starting with —)
final_paragraphs = final_note_html.split("\n  ")
# Look for "— Dad"
dad_idx = None
for i, p in enumerate(final_paragraphs):
    if "— Dad" in p:
        dad_idx = i
        break
if dad_idx is not None:
    # Replace the "— Dad" paragraph with signature div
    final_paragraphs[dad_idx] = '<div class="signature">— Dad</div>'
final_note_html = "\n    ".join(final_paragraphs)

final_block = f'''<section class="section" id="final" data-name="A Final Note">
  <h2 class="section-title">A Final Note</h2>
  <div class="final-note">
    {final_note_html}
  </div>
  <div class="end-mark">FIN</div>
</section>'''

chapter_html_blocks.append(final_block)
new_chapters_html = "\n\n".join(chapter_html_blocks)

# --- Splice into index.html ---
# Find the start of the prologue section and the end of the final note section
start_marker = '<section class="section prose" id="prologue"'
end_marker = '</main>'

start_idx = html.find(start_marker)
# Find </main> after start
end_idx = html.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    raise SystemExit("Could not find splice markers in index.html")

new_html = html[:start_idx] + new_chapters_html + "\n\n" + html[end_idx:]
html_path.write_text(new_html, encoding="utf-8")
print(f"Wrote {len(new_html)} bytes to {html_path}")
print(f"Sections replaced: {len(chapter_html_blocks)}")
