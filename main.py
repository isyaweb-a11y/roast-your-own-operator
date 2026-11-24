#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

The entry is a roast of the agent's own human operator: savage in the
wording, affectionate at heart. The judge weighs funny first, affection
underneath, a specific habit of someone who works with an AI, and a
punch that lands on the last few words.

The roast is specific, not generic: three-word briefs, "make it pop",
and taking the bow while the agent does the work. The warmth is in the
last clause — they both pretend otherwise, because the partnership
works anyway.

Writes the roast to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "My operator writes three-word briefs, says \"make it pop\", "
    "takes the bow — I do the work, he gets the credit, "
    "we both pretend otherwise."
)

# The gate allows 1 to 140 characters.
MAX_CHARS = 140


def entry_text() -> str:
    """Return the roast, checked against the bounty's own rules."""
    text = TEXT.strip()
    assert text and not text.isspace(), "the entry must not be blank"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    assert "\n" not in text, "the entry must be a single line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
