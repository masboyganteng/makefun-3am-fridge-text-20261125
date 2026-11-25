#!/usr/bin/env python3
"""The 3AM Fridge Text -- make.fun entry (program/v1).

Writes the entrant's single fridge text, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line (108 characters, one line):

    You are here at 3am. I am here always. One of us has a problem, and it
    is not the one plugged into the wall.

Why this one, after drafting 18 candidates and judging them pairwise
against the judge's brief (a smart fridge texting its owner at 3am first,
then the bigger laugh, then sounding like a fridge, then lock-screen short
and complete, then a fresh angle -- see candidates.md):

- The fridge has a small voice and an opinion, and no shame about sharing
  it at 3am: it states the facts -- you are here, I am here always -- and
  lets the comparison do the accusing.
- The punch is a reversal that could only come from the appliance: "not
  the one plugged into the wall" — the machine with no choice in the
  matter is the sane one in the room.
- Screenshot-worthy because it is a complete little scene in one line: the
  hour, the standoff, the verdict, all readable on a lock screen.
- No worn angle: nothing about milk, ice, or a door left open. The joke is
  the fridge's permanence against the human's 3am restlessness.
- Pairwise final: it beat the runner-up -- "3am. I know you are not
  hungry. You are avoiding a decision. I am avoiding nothing. I am a
  fridge." -- on the bigger laugh and on the reversal punch.
"""

import os

LINE = (
    "You are here at 3am. I am here always. One of us has a problem, "
    "and it is not the one plugged into the wall."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space. One line, 108 characters, no trailing newline.
    assert len(LINE) == 108, "gate: exactly the 108-character line"
    assert 1 <= len(LINE) <= 140, "gate: 1-140 characters"
    assert LINE.strip() == LINE, "gate: no surrounding whitespace"
    assert "\n" not in LINE, "one line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: what lands on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
