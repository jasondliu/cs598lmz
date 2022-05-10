import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import argparse
import os
import sys
from collections import defaultdict, deque
from datetime import datetime, timedelta
from itertools import chain
from json import loads
from time import time

from gmusicapi import Mobileclient
from gmusicapi.clients import OAUTH_FILEPATH
from gmusicapi.exceptions import NotLoggedIn
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TPE1, TPE2, TALB, TRCK, TCON, APIC, error
from mutagen.mp4 import MP4, MP4Cover
