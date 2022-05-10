import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import os
import sys

from . import _lib

logger = logging.getLogger(__name__)

# TODO: Add thread safety

# TODO: Add error checking to functions


class Connection(object):
    def __init__(self, path):
        self._conn = None
        self._path = path
        self._handle = None
        self._lock = threading.Lock()

    def __enter__(self):
        self._conn = sqlite3.connect(self._path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    def get_handle(self):
        if self._handle is None:
            self._lock.acquire()
            self._handle = _lib.sqlite3_open(self._path.encode())
            self._lock.release()

        return self._handle

    def run(self, sql):
        self._conn.execute(sql)
        self._conn.commit()

    def create_
