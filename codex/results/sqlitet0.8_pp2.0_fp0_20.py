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

class my_sqlite3_dll(ctypes.CDLL):
    def __init__(self, *args, **kwargs):
        super(my_sqlite3_dll, self).__init__(*args, **kwargs)

        self.sqlite3_initialize()

        callable_ = self.sqlite3_progress_handler
        callable_.restype = ctypes.c_int
        callable_.argtypes = [ctypes.c_void_p, ctypes.c_int,
                              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p),
                              ctypes.c_void_p]
        my_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
        self.sqlite3_progress_handler(None, 1000, my_callback, None)

sqlite3.sqlite_version_info = (3, 26, 0)
sqlite3.sqlite_version = "3.26.0
