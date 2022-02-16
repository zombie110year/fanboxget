import json
import math
import os
from pathlib import Path
import re
from typing import List

import requests as r

__version__ = '0.1.0'


class DownloadInfo:
    def __init__(self, json_info: str):
        data = json.loads(json_info)
        self.links: List[str] = data["links"]
        self.origin: str = data["origin"]
        self.href: str = data["href"]
        self.savedir: str = self.href.removeprefix("https://").replace("/", "_")
        self.FANBOXSESSID: str = os.getenv("FANBOXSESSID")
        self.user_agent: str = data["user_agent"]
        self.session = r.Session()
        self.session.headers.update({
            "Cookie": f"FANBOXSESSID={self.FANBOXSESSID};",
            "User-Agent": self.user_agent,
            "Referer": self.origin
        })

    def download(self):
        name_width = math.ceil(math.log10(len(self.links)))
        if not Path(self.savedir).exists():
            Path(self.savedir).mkdir(parents=True)
        for i, link in enumerate(self.links):
            fileext = link.split(".").pop()
            filename = f"{self.savedir}/{i:0{name_width}d}.{fileext}"
            resp = self.session.get(link, timeout=30)
            if resp.status_code == 200:
                Path(filename).write_bytes(resp.content)
                print(f"[fanboxget] {link} -> {filename} downloaded")
            else:
                print(resp.text)
                input()
