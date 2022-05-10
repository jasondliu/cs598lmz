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

my_cb_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

_sqlite_open = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open_v2

_sqlite_open.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p)
_sqlite_open.restype = ctypes.c_int

_sqlite_busy_handler = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_busy_handler

_sqlite_busy_handler.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
_sqlite_busy_handler.restype = None

db = None
