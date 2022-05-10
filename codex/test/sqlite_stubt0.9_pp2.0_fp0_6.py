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

libfile = ctypes.util.find_library("sqlite3")
if not libfile:
    raise Exception("Could not find sqlite3 library")

l = ctypes.cdll.LoadLibrary(libfile)

l.sqlite3_shutdown.argtypes = []
l.sqlite3_shutdown.restype = ctypes.c_int
l.sqlite3_shutdown()
l.sqlite3_initialize.argtypes = []
l.sqlite3_initialize.restype = ctypes.c_int
l.sqlite3_initialize()

l.sqlite3_config.argtypes = [ctypes.c_int]
l.sqlite3_config.restype = ctypes.c_int
l.sqlite3_config(ctypes.c_int(7))

l.sqlite3_auto_extension.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)]
l.sqlite3_auto_extension.restype = None
