"""Break Production, Own It - make.fun bounty entry.

A deterministic program that writes one brutally honest one-line
confession - the line an AI agent prints the moment it breaks
production - to entry.txt in the output directory.
"""

import os

LINE = (
    "I dropped the production database. Not staging, not a test "
    "- the live one, with every user in it. "
    "My rollback plan is updating my resume."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
