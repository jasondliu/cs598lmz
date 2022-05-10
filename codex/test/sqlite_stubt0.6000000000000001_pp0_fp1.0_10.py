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

    return 1000

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(4, 1)
lib.sqlite3_initialize()
lib.sqlite3_open_v2(b"test", ctypes.byref(ctypes.c_void_p(0)), 1|2, None)
lib.sqlite3_create_function_v2(ctypes.c_void_p(0), b"test", 1, 1, ctypes.py_object(my_cb), None, None, None, None)

lib.sqlite3_exec(ctypes.c_void_p(0), b"select test(1);", None, None, ctypes.byref(ctypes.c_void_p(0)))

lib.sqlite3_close_v2(ctypes.c_void_p(0))
lib.sqlite3_shutdown()
