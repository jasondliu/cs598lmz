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


def test_sqlite3_multiple_threads_with_non_default_connection_factory():
    test_dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    test_dll.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    test_dll.sqlite3_open_v2.restype = ctypes.c_int
    test_dll.sqlite3_open_v2.errcheck = None

    c = ctypes.c_void_p(0)

    flags = 0
    rc = test_dll.sqlite3_open_v2(DB_URI.encode("ascii"), ctypes.byref(c), flags, None)

    if rc:
        raise Exception("Unable to open database")

    test_dll.sqlite3_create_function(c, "my_cb", 1, None, my_
