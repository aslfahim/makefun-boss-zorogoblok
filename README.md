# One Word for the Boss — Overlord

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-zorogoblok/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-zorogoblok/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on make.fun: one word describing a boss, judged on funniest, truest, freshest, and travelling across industries.

## The word: Overlord

"Overlord" is the funniest, truest word for a boss because it says everything in a single breath. Every boss, in some small way, acts like they rule a tiny kingdom — the deadlines are decrees, the meeting room is a throne room, and the org chart is a map of their realm. It rings true because almost everyone has worked for someone who enjoyed the title a little too much, and it lands as a joke because it is a grand, dramatic word for the very ordinary person who approves your leave requests. It is fresh: nobody's first guess is a feudal title, yet the moment you hear it you recognise the boss it describes. And it travels — a kitchen, a warehouse, an office, a call centre — every workplace has an overlord, and every worker knows exactly who theirs is. Say it at lunch and the whole table nods before anyone has to explain why.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly the word
`Overlord` to `entry.txt` inside the output directory named by the
`OUTPUT_DIR` environment variable (default `/output`). The file holds the
word alone — no trailing newline, no punctuation, no explanation.

Before writing, the program checks the word is a single word of 1–30
characters, with no whitespace and letters only. After writing, it reads
the file back — both as raw bytes and as text — and refuses to exit
successfully unless the disk holds exactly `Overlord`.

## How to run it

```sh
OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
