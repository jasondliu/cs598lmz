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

sqlite3.sqlite3_open_v2.restype = ctypes.POINTER(ctypes.c_int)
sqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_char_p]
sqlite3.sqlite3_open.restype = ctypes.POINTER(ctypes.c_int)
sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
sqlite3.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(sqlite3.sqlite3_open_v2.restype()), 1, None)

sqlite3.sqlite3_create_function_v2(sqlite3.sqlite3_open_v2.restype, b"test_cb", 0, 1, None, my_cb, None, None, None)

