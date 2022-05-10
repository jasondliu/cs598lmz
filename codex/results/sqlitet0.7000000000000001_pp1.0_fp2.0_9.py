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

def my_cb_deleter(p):
    del my_threading_local.a

    return 10

def main():
    '''
    If this function crashes, the test has passed.
    '''
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    p = ctypes.c_int()
    lib.sqlite3_open_v2("", ctypes.byref(p), sqlite3.OPEN_READWRITE |
        sqlite3.OPEN_CREATE | sqlite3.OPEN_URI, 0)
    assert not p.value
    lib.sqlite3_open_v2("test", ctypes.byref(p), sqlite3.OPEN_READWRITE |
        sqlite3.OPEN_CREATE | sqlite3.OPEN_URI, 0)
    assert not p.value
    lib.sqlite3_open_v2("test", ctypes.byref(p), sqlite3
