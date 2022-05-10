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

cb = sqlite3.sqlite3_progress_handler(my_cb, 100)

sqlite3.sqlite3_progress_handler(cb, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

sqlite3.sqlite3_progress_handler(None, 100, ctypes.c_void_p())

