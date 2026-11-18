# news-image-20261118 entry (Python 3.13, standard library only).
# The front-page image sits beside this file as entry.png; the program
# copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set).
# No network, no randomness: the same bytes come out every run.
# The image is a 1024x1024 newspaper front page: masthead + date line,
# one lead story and six panels, all typeset by the build script.
import os
import shutil
from pathlib import Path

source = Path(__file__).with_name("entry.png")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, out_dir / "entry.png")
