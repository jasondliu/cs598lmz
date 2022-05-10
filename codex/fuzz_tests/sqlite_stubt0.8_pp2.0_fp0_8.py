import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def run_test():
    try:
        path = ctypes.util.find_library("sqlite3")
        if not path:
            return 'skip: sqlite3 not found'

        f = ctypes.CDLL(path).sqlite3_initialize

        f.argtypes = (ctypes.c_int,)
        f.restype = ctypes.c_int

        f(1)

        f = ctypes.CDLL(path).sqlite3_shutdown

        f.argtypes = ()
        f.restype = ctypes.c_int

        f()

        f = ctypes.CDLL(path).sqlite3_config

        f.argtypes = (ctypes.c_int,)
        f.restype = ctypes.c_int

        f(ctypes.c_int.in_dll(ctypes.CDLL(path), "SQLITE_CONFIG_URI"), 0)

        f = ctypes.CDLL(path).sqlite3_config

        f.argtypes = (ctypes.c_int, ctypes.
