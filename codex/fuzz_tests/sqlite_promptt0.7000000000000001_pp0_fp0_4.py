import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("PRAGMA page_size;").fetchone() == (4096,)

class PySqliteCache(threading.local):
    _caches = []
    def __init__(self):
        PySqliteCache._caches.append(self)
        self._cache = {}
        self._lock = threading.Lock()
        self._libc = ctypes.CDLL(ctypes.util.find_library("c"))
    def get(self, key):
        self._lock.acquire()
        try:
            return self._cache[key]
        finally:
            self._lock.release()
    def set(self, key, value):
        self._lock.acquire()
        try:
            self._cache[key] = value
        finally:
            self._lock.release()
    def fget(self, key):
        self._lock.acquire()
        try:
            return self._cache[key]
        finally:
            self._lock.release()
    def fset(self, key, value
