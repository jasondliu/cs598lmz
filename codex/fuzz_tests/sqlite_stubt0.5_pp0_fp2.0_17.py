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

SQLITE_STATIC = ctypes.c_void_p
SQLITE_TRANSIENT = -1

class sqlite3_context(ctypes.Structure):
    pass

class sqlite3_value(ctypes.Structure):
    pass

class sqlite3(ctypes.Structure):
    pass

class sqlite3_stmt(ctypes.Structure):
    pass

sqlite3_open = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open
sqlite3_open.restype = ctypes.c_int
sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(sqlite3))]

sqlite3_close = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_close
sqlite3_close.restype = ctypes.c_int
sqlite3_close.argtypes = [ctypes.POINTER(sqlite3)]

