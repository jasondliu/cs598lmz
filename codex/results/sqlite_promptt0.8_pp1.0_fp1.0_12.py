import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')


RESULT_CACHE_MAX_THREADS = 8
RESULT_CACHE_MAX_RESULTS = 1000


def get_result_cache_lock():
    if not hasattr(get_result_cache_lock, '_lock'):
        get_result_cache_lock._lock = threading.Lock()
    return get_result_cache_lock._lock

class ResultCache(object):
    __slots__ = ('_lock', '_db', '_seq', '_generation', '_cached', '_stale')
    def __init__(self):
        self._lock = get_result_cache_lock()
        self._generation = 0
        self._seq = 0
        self._cached = 0
        self._stale = 0

    def connect(self):
        self._lock.acquire()
        try:
            if self._generation != 0:
                # Already connected.
                return
            self._seq = 0
            self._generation = 1
            self._db = sqlite3.
