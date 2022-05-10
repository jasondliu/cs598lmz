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

def my_cb2(p):
    a = getattr(my_threading_local, "a", None)
    if a:
        a.close()
    return 1

SQLITE_STATIC = 0
SQLITE_TRANSIENT = -1

sqlite_open = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open
sqlite_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite_open.restype = ctypes.c_int

sqlite_close = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_close
sqlite_close.argtypes = [ctypes.c_void_p]
sqlite_close.restype = ctypes.c_int

sqlite_exec = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_exec
