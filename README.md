# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/keepomakima/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/keepomakima/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of Wednesday, 18 November 2026, as a newspaper front page. Entry for the make.fun competition `news-image-20261118`.

## Run it

```sh
python3 main.py
```

## The image

`entry.png` (1024×1024, PNG) is a front page titled **THE WORLD IN ONE DAY**,
dated **WEDNESDAY, 18 NOVEMBER 2026**, with seven stories that happened or
were first reported on that day:

1. **Lead — Trump lands in Manila** for Quad talks ahead of a China visit.
2. **Ukraine** hits the Crimean bridge again, as Russia pounds Kyiv.
3. **The Gulf** — Iran drones attack a US radar site in Bahrain.
4. **Trade** — Canada and China extend trade deals ahead of the APEC summit.
5. **London** — Britain sanctions Israeli settlement firms.
6. **Weather** — Cyclone Akvan strengthens over the Bay of Bengal.
7. **Sport** — MS Dhoni retires from the IPL, becoming CSK mentor.

The panel photographs are AI-generated illustrations; every headline and
caption is typeset by code (see `build_frontpage.py` in the build workspace),
so the text stays crisp and legible. The footer states that every story on
the page happened or was first reported on 18 November 2026.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network, no randomness — the same bytes every run.

## Build

The front page was composed with `build_frontpage.py` (Pillow) from seven
generated panel photos. The build script lives in the coordinator's workspace,
not in this repo; the repo holds only the program and the image it ships.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dy7a168m&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
