import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import signal
import subprocess
import re

from lib.config import config
from lib.util import log

class dnsserver(threading.Thread):

    def __init__(self, libc):
        threading.Thread.__init__(self)
        self.libc = ctypes.CDLL(libc)
        self.libc.setns.argtypes = [ctypes.c_int, ctypes.c_int]
        self.libc.setns.restype = ctypes.c_int
        self.libc.unshare.argtypes = [ctypes.c_int]
        self.libc.unshare.restype = ctypes.c_int
        self.pid = os.getpid()
        self.exit = False
        self.db = sqlite3.connect(config.get('dnslog', 'db'))
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()
        self.cur.execute("CREATE TABLE IF
