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

def test_hook():
    my_db = sqlite3.connect(":memory:")

    if ctypes.util.find_library("sqlite"):
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite"))
        appinit = lib.sqlite3_initialize
        appinit.restype = ctypes.c_int
        appinit.argtypes = []

        my_threading_local.a = None
        appinit()
        lib.sqlite3_open("file:test?mode=memory", ctypes.byref(ctypes.c_void_p(0)))
        lib.sqlite3_commit_hook(ctypes.c_void_p(0), ctypes.py_object(my_cb))
        lib.sqlite3_close(ctypes.c_void_p(0))

        if my_threading_local.a is not None:
            # this is the case that fails
            my_threading_local.a.close()
        else:
            print("a is None
