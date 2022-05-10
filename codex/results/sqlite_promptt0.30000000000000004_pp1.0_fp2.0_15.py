import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class SQLite3:
    def __init__(self, filename, timeout=5.0):
        self._db = sqlite3.connect(filename, timeout=timeout)
        self._db.row_factory = sqlite3.Row
        self._db.text_factory = str
        self._lock = threading.Lock()

    def execute(self, query, *args):
        with self._lock:
            return self._db.execute(query, args)

    def executemany(self, query, *args):
        with self._lock:
            return self._db.executemany(query, args)

    def commit(self):
        with self._lock:
            return self._db.commit()

    def rollback(self):
        with self._lock:
            return self._db.rollback()

    def fetchone(self, query, *args):
        with self._lock:
            return self._db.execute(query, args).fetchone()

    def fetchall(self, query, *args):
       
