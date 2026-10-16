#!/usr/bin/env python3
"""Builds the GitHub wiki from the files in this repository.

docs/USER-GUIDE.md stays the single source: each "## N. Title" section becomes
a wiki page, and BENCHMARKS.md and CHANGELOG.md become pages of their own.
Image paths and links between sections are rewritten for the wiki.

    scripts/build-wiki.py <wiki checkout>

then commit and push the wiki checkout.
"""
import re
import sys
from pathlib import Path

REPO = "True2456/Rindi-Agent-releases"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
BLOB = f"https://github.com/{REPO}/blob/main"
root = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1])


def anchor(heading: str) -> str:
    """GitHub's heading anchor: lowercase, punctuation dropped, spaces to hyphens."""
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")


def page_name(title: str) -> str:
    return re.sub(r"[^\w]+", "-", title).strip("-")


guide = (root / "docs/USER-GUIDE.md").read_text()
intro, *sections = re.split(r"(?m)^## (?=\d+\. )", guide)

pages = []          # (file name, title, body)
anchors = {         # guide anchor -> wiki link target
    "reporting-problems": f"https://github.com/{REPO}/issues",  # a README heading
}
for section in sections:
    heading, body = section.split("\n", 1)
    title = re.sub(r"^\d+\.\s*", "", heading).strip()
    name = page_name(title)
    anchors[anchor(heading)] = name
    for sub in re.findall(r"(?m)^#{3,4} (.+)$", body):
        anchors[anchor(sub)] = f"{name}#{anchor(sub)}"
    body = re.sub(r"(?m)^---\s*$", "", body).strip()
    body = re.sub(r"(?m)^###", "##", body)
    pages.append((name, title, body))


def rewrite(text: str) -> str:
    text = re.sub(r"\]\((?:docs/)?images/", f"]({RAW}/docs/images/", text)
    text = re.sub(r"\]\(#([\w\-]+)\)", lambda m: f"]({anchors.get(m[1], '#' + m[1])})", text)
    text = re.sub(r"\]\((?:docs/)?USER-GUIDE\.md#([\w\-]+)\)", lambda m: f"]({anchors.get(m[1], 'Home')})", text)
    text = re.sub(r"\]\((?:docs/)?USER-GUIDE\.md\)", "](Home)", text)
    text = re.sub(r"\]\((?:\.\./)?BENCHMARKS\.md(#[\w\-]+)?\)", lambda m: f"](Benchmarks{m[1] or ''})", text)
    text = text.replace("](CHANGELOG.md)", "](Release-notes)")
    text = re.sub(r"\]\((benchmarks/[^)]+)\)", lambda m: f"]({BLOB}/{m[1]})", text)
    return text


out.mkdir(parents=True, exist_ok=True)
for old in out.glob("*.md"):
    old.unlink()

for name, title, body in pages:
    (out / f"{name}.md").write_text(rewrite(body) + "\n")

for source, name in (("BENCHMARKS.md", "Benchmarks"), ("CHANGELOG.md", "Release-notes")):
    text = (root / source).read_text()
    text = re.sub(r"\A# .+\n+", "", text)          # the wiki shows the page name as its title
    (out / f"{name}.md").write_text(rewrite(text))

readme = (root / "README.md").read_text()
summary = readme.split("\n## ", 1)[0]
summary = re.sub(r"\A# .+\n+", "", summary)
# The README's short benchmarks section, so Home shows it too.
benchmarks = re.search(r"(?ms)^## Benchmarks\n(.*?)(?=^## )", readme)[1].strip()
contents = "\n".join(f"{i}. [{title}]({name})" for i, (name, title, _) in enumerate(pages, 1))
(out / "Home.md").write_text(rewrite(summary).strip() + f"""

**[Download the latest version](https://github.com/{REPO}/releases)** · [Benchmarks](Benchmarks) · [Release notes](Release-notes) · [Report a problem](https://github.com/{REPO}/issues)

## Benchmarks

{rewrite(benchmarks)}

## User guide

{contents}
""")

sidebar = "\n".join(f"- [{title}]({name})" for name, title, _ in pages)
(out / "_Sidebar.md").write_text(f"""**[Home](Home)**

**User guide**

{sidebar}

**More**

- [Benchmarks](Benchmarks)
- [Release notes](Release-notes)
- [Downloads](https://github.com/{REPO}/releases)
""")
(out / "_Footer.md").write_text(
    f"Generated from [docs/USER-GUIDE.md]({BLOB}/docs/USER-GUIDE.md) by `scripts/build-wiki.py`. "
    "Edit the files in the repository, not these pages.\n")
print(f"{len(pages) + 3} pages written to {out}")
