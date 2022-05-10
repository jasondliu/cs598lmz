import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class InvalidateCall:
    def __init__(self, on_invalidate):
        self.on_invalidate = on_invalidate
        self.lock = threading.Lock()
        self.active = None
        self.cache = None

    def __call__(self, *args):
        with self.lock:
            if self.active is not None and self.active is not args:
                self.active = None
                self.cache = None
            self.on_invalidate()
            if self.cache is None:
                self.active = args
                self.cache = self.__call__(*args)
            return self.cache

# This is not threadsafe and is merely a performance optimization.
# It is threadsafe in the sense that it will always return the same result.
# However, it will not return the right result if the user changes the
# value that it is caching.
@InvalidateCall
def load_libc():
    libc_name = ctypes.util.find_library("c")
    assert libc
