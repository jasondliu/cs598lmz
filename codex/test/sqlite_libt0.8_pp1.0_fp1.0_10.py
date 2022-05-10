import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import sys
import os
import traceback
import os.path
import glob

class Cache:
    def __init__(self, sqlite_file, force=False):
        self.lock = threading.Lock()

        self.sqlite_file = sqlite_file
        self.cache_file = sqlite_file.replace('.db', '.cache')
        self.cache_exists = os.path.isfile(self.cache_file)
        self.force = force

    def __enter__(self):
        self.lock.acquire()
        self.sqlite = sqlite3.connect(self.sqlite_file)
        self.sqlite.row_factory = sqlite3.Row
        self.cursor = self.sqlite.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        if not exc_type:
            self.sqlite.commit()
        self.sqlite.close()
