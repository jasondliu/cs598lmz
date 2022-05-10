import ctypes
import ctypes.util
import threading
import sqlite3

from . import _common
from . import lib
from . import _compat
from . import _sqlite
from . import _sqlite_ops
from . import _sqlite_lock


class _SQLiteConnection(object):
    def __init__(self, conn):
        self._conn = conn

    def close(self):
        self._conn.close()
        self._conn = None

    def cursor(self):
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __del__(self):
        if self._conn:
            self.close()

    def __getattr__(self, name):
        return getattr(self._conn, name)


class _SQLiteLock(object):
    def __init__(self, path):
        self._lock = _sqlite_lock.SQLite
