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

def test_callback():
    _sqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
    _sqlite.sqlite3_initialize()
    _sqlite.sqlite3_config(ctypes.c_int(1), ctypes.c_void_p(1))
    _sqlite.sqlite3_config(ctypes.c_int(2), ctypes.c_void_p(1))
    _sqlite.sqlite3_config(ctypes.c_int(3), ctypes.c_void_p(1))
    _sqlite.sqlite3_config(ctypes.c_int(4), ctypes.c_void_p(1))
    _sqlite.sqlite3_config(ctypes.c_int(5), ctypes.c_void_p(1))
    _sqlite.sqlite3_config(ctypes.c_int(6), ctypes.c_void_p(1))
    _sqlite.sqlite3_config
