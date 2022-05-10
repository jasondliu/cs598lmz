import ctypes
import ctypes.util
import threading
import sqlite3

from .util import (clib,
                   resolve_path)

_libsqlite3_path = ctypes.util.find_library('sqlite3')
assert _libsqlite3_path is not None, 'sqlite3 library not found'
_libsqlite3 = ctypes.cdll.LoadLibrary(_libsqlite3_path)

class sqlite3_db:
    __slots__ = ['_db']

    def __init__(self, db_path = None):
        if db_path:
            self._db = sqlite3.connect(db_path)
        else:
            self._db = sqlite3.connect(':memory:')
        self._db.row_factory = sqlite3.Row

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._db.close()
        return False

    def get_row_value(self, row, index, as_str=True):
        value = row[index]
