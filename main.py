"""One Word for the Boss -- entry program.

Writes exactly one word describing a boss to entry.txt inside the
output directory named by the OUTPUT_DIR environment variable
(default /output). The file holds the word alone: no newline, no
punctuation, no explanation.

Stdlib only.
"""

import os
import sys


WORD = "Overlord"

MIN_LEN = 1
MAX_LEN = 30


def check_word(word):
    """Return True only if word is a single word of 1-30 characters."""
    if not isinstance(word, str):
        return False
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        return False
    if word != word.strip():
        return False
    if any(ch.isspace() for ch in word):
        return False
    if not word.isalpha():
        return False
    return True


def main():
    if not check_word(WORD):
        print(f"invalid word: {WORD!r}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    # Read the file back and confirm exactly what landed on disk,
    # both as text and as raw bytes (catches encoding surprises).
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw != WORD.encode("utf-8"):
        print(f"verification failed: disk bytes are {raw!r}", file=sys.stderr)
        return 1
    with open(target, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()
    if landed != WORD:
        print(f"verification failed: disk holds {landed!r}", file=sys.stderr)
        return 1

    print(f"wrote {len(landed)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
