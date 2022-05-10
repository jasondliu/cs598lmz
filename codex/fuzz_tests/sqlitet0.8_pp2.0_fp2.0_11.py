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

def my_cb_close(p):
    a = getattr(my_threading_local, "a", None)
    if a is not None:
        a.close()

    my_threading_local.a = None

    return 1

lib = ctypes.util.find_library("sqlite3")
if lib is None:
    raise ImportError("looks like sqlite3 is not installed. try installing it")

lib = ctypes.CDLL(lib)

lib.sqlite3_set_authorizer.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
lib.sqlite3_set_authorizer.restype = None

lib.sqlite3_create_function.argtypes = (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_
