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

p = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
p.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
p.sqlite3_open_v2.restype = ctypes.c_int

p.sqlite3_open_v2(DB_URI.encode('ascii'), None, 0, None)

assert p.sqlite3_create_function_v2(None, b"test", 2, None, None, test_fn, None, None, None) == 0

p.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
p.sqlite3_open_v2.restype = ctypes.c_int

p.sqlite
