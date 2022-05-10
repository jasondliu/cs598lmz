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

def my_cb_2(p):
    return 1

class Thread(threading.Thread):
    def __init__(self, fn):
        threading.Thread.__init__(self)
        self.fn = fn

    def run(self):
        self.fn()

def test_callback():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table test (x)")

    lib.sqlite3_open_v2.restype = ctypes.c_void_p
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p]

    lib.sqlite3_create_function_v2.restype = ctypes.c_int
    lib.sqlite3_create_function_v2.argtypes
