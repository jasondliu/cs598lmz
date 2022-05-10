import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re
import logging

from . import utils
from . import config

log = logging.getLogger(__name__)

#
# SQLite3
#

class SQLite3(object):
    def __init__(self, filename):
        self.filename = filename
        self.db = None
        self.lock = threading.Lock()
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.filename, timeout=config.SQLITE_TIMEOUT)

    def execute(self, query, args=None):
        with self.lock:
            try:
                if args:
                    return self.db.execute(query, args)
                else:
                    return self.db.execute(query)
            except sqlite3.OperationalError as e:
                if e.args[0] == 'database is locked':
                    self.connect()
                    return self.execute(query, args)
                else:
                    raise

