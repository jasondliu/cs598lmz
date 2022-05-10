import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
import sys

class Sqlite3Lock:
    def __init__(self, db, lock_type):
        self.db = db
        self.lock_type = lock_type

    def __enter__(self):
        self.db.execute(f"PRAGMA lock_status;")
        self.db.execute(f"PRAGMA {self.lock_type} lock;")
        return self

    def __exit__(self, type, value, traceback):
        self.db.execute(f"PRAGMA unlock_all;")
        self.db.execute(f"PRAGMA lock_status;")

class Sqlite3:
    def __init__(self, path, shared_cache=False):
        self.shared_cache = shared_cache
        if shared_cache:
            self.db = sqlite3.connect(f'file:{path}?cache=shared', uri=True)
        else:
            self.db = sqlite3.connect(path)
        self.lock
