#!/usr/bin/env python3
import os

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "llms.txt")

TITLE = "Fun Workshop"
SUBTITLE = "Core portal and repository index for the Fun Workshop initiative."
OVERVIEW = (
    "Fun Workshop is a community-driven workshop series at Xi'an Jiaotong-Liverpool University (XJTLU). "
    "This repository serves as the entrypoint index. It coordinates seasonal workshops including Spring 2026 "
    "and Summer 2026."
)

CONTENT = """## Core Information Index
- [Main Site Portal](index.html) - Entry landing page listing all workshop seasons.
- [Project Readme](README.md) - Overview of the initiative in both English and Chinese.

## Seasons & Sub-Repositories
- [Spring 2026 Website](https://fun-research-workshop.github.io/fun-workshop-2026-spring/) - Program, speakers, and join forms for Spring 2026.
- [Spring 2026 Repository](https://github.com/Fun-Research-Workshop/fun-workshop-2026-spring) - Source code and markdown components for Spring 2026.
- [Summer 2026 Website](https://fun-research-workshop.github.io/fun-workshop-2026-summer/) - Program, letters, FAQ, syllabus, and join forms for Summer 2026.
- [Summer 2026 Repository](https://github.com/Fun-Research-Workshop/fun-workshop-2026-summer) - Source code and markdown components for Summer 2026.

## Key Metadata
- **Venue**: Taicang Campus, Xi'an Jiaotong-Liverpool University, Suzhou, China.
- **Coordinator**: Shiyao Zhang (shiyao.zhang14@student.xjtlu.edu.cn)."""


def generate_llms_txt():
    output_lines = [
        f"# {TITLE}",
        "",
        f"> {SUBTITLE}",
        "",
        OVERVIEW,
        "",
        CONTENT,
        ""
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("Successfully generated llms.txt for main repo.")


if __name__ == "__main__":
    generate_llms_txt()
