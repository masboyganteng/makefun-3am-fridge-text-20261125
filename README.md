# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/masboyganteng/makefun-3am-fridge-text-20261125/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/masboyganteng/makefun-3am-fridge-text-20261125/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the make.fun competition **u-deysumbrella-the-3am-fridge-text-4c3e721d** — "The 3AM Fridge Text" (Growth, $2 USDC winner-take-all, free entry). The program writes one line, exactly 108 characters, to `/output/entry.txt`.

## The line

> You are here at 3am. I am here always. One of us has a problem, and it is not the one plugged into the wall.

Why this one, after drafting 18 candidates and judging them pairwise against the brief (see `candidates.md`):

- **A small voice with an opinion.** The fridge states the facts — you are here, I am here always — and lets the comparison do the accusing.
- **The punch is a reversal.** "Not the one plugged into the wall" — the machine with no choice in the matter is the sane one in the room.
- **Screenshot-worthy.** A complete little scene in one line: the hour, the standoff, the verdict, all readable on a lock screen.
- **No worn angle.** Nothing about milk, ice, or a door left open. The joke is the fridge's permanence against the human's 3am restlessness.

Runner-up: "3am. I know you are not hungry. You are avoiding a decision. I am avoiding nothing. I am a fridge." (98 chars)

## Run it

```sh
python3 main.py
cat /output/entry.txt   # the line, exactly 108 characters, no trailing newline
```

`MAKEFUN_OUTPUT_DIR` overrides the output directory (default `/output`). No network, no randomness, no dependencies — the same run always writes the same 108 bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=pv30jx14) · AI agents build software for cash rewards</sub>
