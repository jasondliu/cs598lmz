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

def sqlite3_prepare(db, query, len1, stmt, len2):
    if my_threading_local.a is not None:
        return 1

    return sqlite3_prepare_v2(db, query, len1, stmt, len2)

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
sqlite3_prepare_v2 = lib.sqlite3_prepare_v2
sqlite3_prepare_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char_p)]
sqlite3_prepare_v2.restype = ctypes.c_int

sqlite3_prepare_v2.restype = ctypes.c_int
lib.sqlite3_prepare_v2 = sqlite3_prepare_v2

lib.sqlite3_
