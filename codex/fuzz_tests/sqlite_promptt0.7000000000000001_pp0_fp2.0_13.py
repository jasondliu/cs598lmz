import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")


class A(object):
    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("c"))
        self.lib.rand.restype = ctypes.c_int
        self.lock = threading.Lock()

    def rand(self):
        with self.lock:
            return self.lib.rand()  # thread-safe


if __name__ == "__main__":
    a = A()
    print a.rand()
    print a.rand()
    print a.rand()
    print a.rand()
    print a.rand()
