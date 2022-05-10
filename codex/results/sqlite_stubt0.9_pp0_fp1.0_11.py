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

sqlext = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

sqlext.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
sqlext.sqlite3_open_v2.restype = ctypes.c_int

sqlext.sqlite3_create_disposable_module.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
sqlext.sqlite3_create_disposable_module.restype = ctypes.c_int

sqlext.sqlite3_disposable_initialize.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
sqlext.sqlite3_disposable_initialize.restype
