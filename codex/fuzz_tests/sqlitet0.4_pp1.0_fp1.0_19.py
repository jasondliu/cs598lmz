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

def test_init():
    # load the sqlite3 library
    lib = ctypes.util.find_library("sqlite3")
    if not lib:
        raise Exception("sqlite3 library not found")
    lib = ctypes.cdll.LoadLibrary(lib)

    # set up the sqlite3_open_v2 function prototype
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    lib.sqlite3_open_v2.restype = ctypes.c_int

    # create a callback function
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    # create a database
    db = ctypes.c_void_p()
    lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(db), sqlite3.SQLITE
