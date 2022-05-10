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

    return 10


def make_cb():
    return sqlite3.sqlite3_progress_handler(ctypes.c_int(), ctypes.c_void_p())

def test_cb():
    cb = make_cb()
    cb.argtypes = [ctypes.c_void_p]
    cb.restype = ctypes.c_int

    cb.errcheck = lambda result, func, args: args[0]

    p = sqlite3.sqlite3_progress_handler(cb, None)
    p.value = ctypes.c_void_p(ctypes.cast(p.value, ctypes.c_void_p).value)

    cb = make_cb()
    cb.argtypes = [ctypes.c_void_p]
    cb.restype = ctypes.c_int

    cb.errcheck = lambda result, func, args: args[0]

    p = sqlite3.sqlite3_progress_handler(cb, None)
