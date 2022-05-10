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

SQLITE_LIB = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

SQLITE_OPEN = SQLITE_LIB.sqlite3_open_v2
SQLITE_OPEN.argtypes = [ctypes.c_char_p,                                                       ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
SQLITE_OPEN.restype = ctypes.c_int

SQLITE_PREPARE = SQLITE_LIB.sqlite3_prepare_v2
SQLITE_PREPARE.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char_p)]
SQLITE_PREPARE.restype = ctypes.c_int

SQLITE_CLOSE = SQLITE_LIB.sqlite3_close_v2
SQLITE_CLOSE.argtypes = [
