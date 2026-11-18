# news-image-20261118 entry, round v2 (Python 3.13, standard library only).
# The v2 front-page image sits beside this file as entry.png; the program
# copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set).
# No network, no randomness: the same bytes come out every run.
# The image is a 1024x1024 newspaper front page: "THE WORLD TODAY"
# masthead, Gulf-strikes lead, four photo panels, a world-map panel and
# a 13-item briefs column — 18 stories from five continents.
# v2 replaces the v1 front page ("THE WORLD IN ONE DAY", Trump/Manila lead)
# with a new lead, new nameplate, a map panel and a denser story count.
import os
import shutil
from pathlib import Path

source = Path(__file__).with_name("entry.png")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, out_dir / "entry.png")
