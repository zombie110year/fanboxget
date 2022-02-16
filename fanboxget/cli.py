import argparse
import os
import sys
from pathlib import Path

from . import DownloadInfo

DESCRIPTION = """Need a ENV VAR named 'FANBOXSESSID' to login.
For example:

export FANBOXSESSID=80234606_4asdfasdfdsCfkDEz1uHZadcshlZrQ6M
fanboxget downloadinfo.json

The downloadinfo.json looks like:
{
    "links": [
        "<image url>",
        ...
    ],
    "origin": "https://<creator>.fanbox.cc/posts/<artwork id>/"
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50"
}
"""

def parser():
    p = argparse.ArgumentParser(description=DESCRIPTION)
    p.add_argument("FILE", help="JSON file path.", nargs="?")
    return p

def main():
    args = parser().parse_args()
    assert os.getenv("FANBOXSESSID") is not None, "need envvar 'FANBOXSESSID'"
    if args.FILE is None:
        download_info = sys.stdin.read()
    else:
        download_info = Path(args.FILE).read_text("utf-8")
    di = DownloadInfo(download_info)
    di.download()
