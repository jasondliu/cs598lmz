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
    if my_threading_local.a:
        my_threading_local.a.cursor().execute("SELECT t(n,n) FROM (SELECT 1 AS n UNION ALL SELECT 2)").test()
    return 0

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(sqlite3.Connection))]
lib.sqlite3_open.restype = int

lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(sqlite3.Connection)), ctypes.c_int, ctypes.c_char_p]
lib.sqlite3_open_v2.restype = int

lib.sqlite3_close.argtypes = [ctypes.POINTER(sqlite3.Connection)]
lib.sqlite3_close.restype
