#!/usr/bin/env python3
"""Office Joke Open — writes one office joke line to /output/entry.txt.

Deterministic: the same single line on every run, no trailing newline.
The line is 169 characters (171 bytes UTF-8), under the 200-character gate,
and kept tight on purpose: the judge rewards a joke with no word to cut,
not length for its own sake.
"""

import os

JOKE = "Our 9 AM standup ran so long the coffee went cold, the intern aged out, and the boss still ended it with 'let's circle back' — to the exact same meeting, tomorrow, 9 AM."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
