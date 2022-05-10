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

def my_cb2(a, b, c):
    p = ctypes.cast(a, ctypes.py_object).value
    return 1

def make_test():
    cdll = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
    foo = cdll.sqlite3_enable_shared_cache
    foo.argtypes = [ctypes.c_int]
    foo.restype = ctypes.c_int

    if cdll.sqlite3_threadsafe() == 2:
        c_fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
        c_fn2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)

        foo = cdll.sqlite3_pre_initialize_app
        foo.argtypes = [c_fn]
        foo.restype = ctypes.c_int


