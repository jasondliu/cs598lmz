import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:test.db?mode=memory&cache=shared", uri=True)

class Spinlock:
    """
    Spins until we get a lock, then hold it.
    """
    def __init__(self):
        self._lock = threading.RLock()

    def __enter__(self):
        self._lock.acquire()

    def __exit__(self, typ, value, traceback):
        self._lock.release()


class SharedCacheConnection(sqlite3.Connection):
    """
    Shared cache connection.
    """

    _cachedict = {"Spinlock": Spinlock()}

    def __init__(self, uri=False, check_same_thread=True, timeout=5.0):
        """
        Initialize a shared cache connection.
        """
        self._cachedict = self.__class__._cachedict
        self._lock = self._cachedict["Spinlock"]
        self.__timeout = timeout
        self._timeout = timeout
        self._timeout_in_ms = int(timeout *
