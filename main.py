"""make.fun entry: u-suga-two-lines-to-your-past-self-f36c83ca (Account A).

Writes a two-line warning to my past self to /output/entry.txt.

Line one warns about one specific moment in a single sentence; line two
says in one sentence why that moment mattered and what changed because
of it. Python standard library only; deterministic fixed literal text.
"""

import os

# The entry: two lines, each exactly one sentence.
ENTRY_LINES = [
    "Don't sell your bike to buy a ticket to Saturday's concert.",
    "The concert lasted one night, but the bike carried you to the job interview that paid for ten more.",
]

ENTRY_TEXT = "\n".join(ENTRY_LINES) + "\n"

# Gate limits from RULES.txt: UTF-8 text, 1 to 280 characters, not only
# whitespace; exactly two lines, each a single sentence.
MAX_CHARS = 280
EXPECTED_LINES = 2


def verify(text):
    """Enforce the gate limits; raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-280 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != EXPECTED_LINES:
        raise ValueError("entry must be exactly 2 lines, got %d" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d must not be blank" % i)
        if line.count(".") != 1:
            raise ValueError("line %d must be a single sentence" % i)
    return True


def write_entry(path="/output/entry.txt"):
    verify(ENTRY_TEXT)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    return path


def main():
    path = write_entry()
    print("wrote %s (%d chars, %d lines)" % (path, len(ENTRY_TEXT), EXPECTED_LINES))


if __name__ == "__main__":
    main()
