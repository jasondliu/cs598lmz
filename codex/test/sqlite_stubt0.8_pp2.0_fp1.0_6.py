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

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p)).in_dll(
    ctypes.CDLL(ctypes.util.find_library('sqlite3')),
    'sqlite3_open_v2'
)

my_cb_p.errcheck = None
my_cb_p.restype = ctypes.c_int
my_cb_p.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]
my_cb_p.argtypes = [ctypes.c_void_p]

my_cb_p.errcheck = None

my_cb_p.restype = ctypes.c_int
my_cb_p.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

