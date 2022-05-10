from lzma import LZMADecompressor
LZMADecompressor.MAX_LENGTH = int(999e9)
import json
import os
from copy import deepcopy
from pathlib import Path
from importlib import util
from urllib.request import urlopen
from shutil import rmtree
from zipfile import ZipFile
from pprint import pprint

from blaseball_mike.config import CONFIG
from blaseball_mike.util import get_lzma_url


# https://blaseball.com/resources/snapshots
FILENAMES = {
    "teams": "teams.json",
    "divisions": "divisions.json",
    "subs": "subs.json",
    "leagues": "leagues.json",
    "lineups": "lineups.json",
    "games": "games.json",
    "standings": "standings.json",
    "players": "players.json",
    "blessings": "blessings.json",
    "decrees": "decrees.json",
    "incidents": "incidents.json",
    "seasons":
