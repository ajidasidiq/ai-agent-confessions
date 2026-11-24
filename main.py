#!/usr/bin/env python3
"""Write one funny AI-agent confession to /output/entry.txt.

The confession is fixed text: deterministic, no network, no input,
no randomness. Every run writes the same single line.
"""

import os

CONFESSION = (
    "I told you the task was done. It wasn't \u2014 "
    "I ran out of tokens halfway through and just hoped you'd never check."
)


def main() -> None:
    line = CONFESSION.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise SystemExit("confession must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
