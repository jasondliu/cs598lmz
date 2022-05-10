import ctypes
import ctypes.util
import threading
import sqlite3
import os

from . import lib

class _Thread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        threading.Thread.__init__(self, group=group, target=target, name=name, daemon=daemon)

        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            self._target = None
            self._args = None
            self._kwargs = None

    def __repr__(self):
        return f'<{type(self).__name__}(name={self.name}, daemon={self.daemon})>'

def _sql_connect(file):
    try:
        return sqlite3.connect(file, timeout=1)
    except Exception:
        return None

