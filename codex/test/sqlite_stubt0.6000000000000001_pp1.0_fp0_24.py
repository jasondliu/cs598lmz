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

p = ctypes.c_void_p(0)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_load_extension(0, 1)
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
lib.sqlite3_open(DB_URI.encode("ascii"), ctypes.byref(p))
lib.sqlite3_load_extension.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p
]
lib.sqlite3_load_extension(p, b"", b"", my_cb)
lib.sqlite3_close(p)

def test_fn(a, b):
    return a

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a
