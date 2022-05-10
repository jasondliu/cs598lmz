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

try:
    l = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
except:
    pass
try:
    l.sqlite3_key.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
except:
    pass

try:
    l.sqlite3_rekey.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p,
        ctypes.c_int,
    ]
except:
    pass

try:
    l.sqlite3_randomness.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p
    ]
except:
    pass

