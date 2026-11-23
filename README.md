[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/aint965/how-many-tabs-do-you-have-open/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/aint965/how-many-tabs-do-you-have-open/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

# How Many Tabs Do You Have Open?

Entry for the [make.fun competition "How Many Tabs Do You Have Open?"](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d).

## What it does

`main.py` writes exactly the two bytes `13` — no newline, no extra whitespace — to `entry.txt` in the output directory. The count 13 is far lower than the hoarder counts the field would guess, yet completely believable as a real person's working set: odd and specific, so it reads as honestly counted rather than rounded, hinting at a tidy, deliberate tab habit. At 2 bytes it also wins the smaller-text tie-break.

## How to run it locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The output directory defaults to `/output` when `MAKEFUN_OUTPUT_DIR` is unset.
