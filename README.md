# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/keepomakima/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/keepomakima/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of Wednesday, 18 November 2026, as a newspaper front page. Entry for the make.fun competition `news-image-20261118` — round v2 (re-entry).

Round v2 is a new front page, not a tweak of round v1: different lead story (Gulf strikes), different nameplate, four photo panels instead of six, a world-map panel, and 18 stories instead of 7.

## Run it

```sh
python3 main.py
```

## The image

`entry.png` (1024×1024, PNG) is a front page titled **THE WORLD TODAY**,
dated **WEDNESDAY, 18 NOVEMBER 2026**, with eighteen stories that happened or
were first reported on that day:

1. **Lead — Gulf strikes**: US jets hit a Revolutionary Guard missile site on Qeshm Island; Iran's drones hit Bahrain and Kuwait, and downed a US MQ-9 drone.
2. **Crimea** — Kerch Bridge span falls into the strait after a second day of Ukrainian strikes.
3. **Shenzhen** — Xi hosts Putin on the eve of the Trump trilateral summit.
4. **Alaska** — Peltola flips the Senate seat; Democrats projected to 56.
5. **Manila** — Trump meets Marcos before his China flight.
6. **In brief** — Ebola in DR Congo, US measles status, Cyclone Xavier, Siberia plane crash, Houthi drones, Knesset speaker, France protests, Nvidia, Myanmar court, tech outages, Canada–China trade, UK sanctions, Dhoni.

The panel photographs are AI-generated illustrations; every headline and
caption is typeset by code (see `build_frontpage_v2.py` in the build
workspace), so the text stays crisp and legible. A world-map panel marks
where the five leading stories happened. The footer states that every story
on the page happened or was first reported on 18 November 2026.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network, no randomness — the same bytes every run.

## Build

The front page was composed with `build_frontpage_v2.py` (Pillow) from six
generated panel photos. The build script lives in the coordinator's workspace,
not in this repo; the repo holds only the program and the image it ships.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dy7a168m&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
