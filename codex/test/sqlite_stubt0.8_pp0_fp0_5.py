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

def _sqlite_import():
    clib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    clib.sqlite3_register_functable.restype = ctypes.c_int
    clib.sqlite3_register_functable.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    clib.sqlite3_register_functable(my_cb, None)

def test_leak():
    import gc

    gc.collect()

    num_objects_before = len(gc.get_objects())

    _sqlite_import()

    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    gc.collect()

    num_objects_after = len(gc.get_objects())

