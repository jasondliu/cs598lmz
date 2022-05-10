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

# This function will be called everytime a new connection is opened.
sqlite3.sqlite3_open_v2.errcheck = lambda p: sqlite3.sqlite3_open(":memory:", p)
sqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

sqlite3.sqlite3_enable_load_extension(ctypes.c_void_p(None), 0)
sqlite3.sqlite3_load_extension.restype = None
sqlite3.sqlite3_load_extension.errcheck = lambda res, fun, p: res or None
sqlite3.sqlite3_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]

sqlite3.sqlite3_extension_init.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
sqlite3
