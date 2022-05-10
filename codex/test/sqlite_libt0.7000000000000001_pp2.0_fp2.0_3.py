import ctypes
import ctypes.util
import threading
import sqlite3
import re
import sys
import urllib2
import json
import Queue
import traceback
import datetime
import time

from . import settings
from . import util
from . import db
from . import log

class Downloader(threading.Thread):
    def __init__(self):
        super(Downloader, self).__init__()
        self.daemon = True
        self.queue = Queue.Queue()
        self.downloading = threading.Event()
        self.cancelled = False
        self.downloading_bytes = 0
        self.total_bytes = 0
        self.downloading_perc = 0
        self.downloading_title = None
        self.downloading_icon = None
        self.downloading_artist = None
        self.downloading_url = None
        self.downloading_track = None
        self.downloading_num = 0
        self.downloading_total = 0
        self.finished_downloading = threading.Event()
        self.finished_downloading.set()
        self.start()
