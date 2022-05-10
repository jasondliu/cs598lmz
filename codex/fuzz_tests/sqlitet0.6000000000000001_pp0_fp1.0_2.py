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

def my_cb2(p1, p2, p3):
    return 1

def my_cb3(p1, p2):
    return 1

def my_cb4(p):
    return 1

sqlite3.sqlite3_initialize()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open.restype = ctypes.c_int
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

filename = ctypes.create_string_buffer(b"test")

db = ctypes.c_void_p()
lib.sqlite3_open(filename, ctypes.byref(db))

p = ctypes.c_void_p()

lib.sqlite3_create_function(db, b"test2", 3, ctypes.c_int(), None, my_cb2, None, None)
lib.sqlite3_create_function
