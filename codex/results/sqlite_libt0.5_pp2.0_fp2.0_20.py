import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import signal
import select
import errno
from util import *
import config
import logging
import logging.config

class Fuse(object):
    def __init__(self, mountpoint, foreground=False, ro=False, allow_other=False):
        self.mountpoint = os.path.abspath(mountpoint)
        self.foreground = foreground
        self.ro = ro
        self.allow_other = allow_other
        self.fd = None
        self.thread = None
        self.conn = None
        self.db_conn = None
        self.db_conn_lock = threading.Lock()
        self.thread_lock = threading.Lock()
        self.thread_cond = threading.Condition(self.thread_lock)
        self.stopped = False
        self.stopped_lock = threading.Lock()
        self.stopped_cond = threading.Condition(self.stopped_lock)
        self.raw_fi_lock = threading.Lock()
        self.raw_fi
