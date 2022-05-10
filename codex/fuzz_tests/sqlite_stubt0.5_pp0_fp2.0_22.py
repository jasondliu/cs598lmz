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

def test_cb():
    p = ctypes.c_void_p()
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_SaveThread()
    r = sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p),
                                sqlite3.SQLITE_OPEN_READWRITE |
                                sqlite3.SQLITE_OPEN_CREATE, None)
    if r != sqlite3.SQLITE_OK:
        raise Exception("could not open database")
    r = sqlite3.sqlite3_create_function_v2(p, b"my_cb", 1,
                                           sqlite3.SQLITE_UTF8,
                                           None, my_cb, None, None, None)
    if r != sqlite3.SQLITE_OK:
        raise Exception("could not create function")
    r = sqlite3.sqlite3_exec(p, b"SELECT my_cb()", None, None, None)
    if
