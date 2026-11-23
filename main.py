#!/usr/bin/env python3
"""Six Words, One Story: write one complete six-word story to /output/entry.txt.

The story is a single concrete scene opened mid-moment: letters keep
arriving after the woman who wrote them is already gone. The turn lands
in the last two words, and what the letters say is left for the reader.
Pure stdlib, deterministic, no network at runtime.
"""

import os

STORY = "Grandma's letters arrived after her funeral."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
