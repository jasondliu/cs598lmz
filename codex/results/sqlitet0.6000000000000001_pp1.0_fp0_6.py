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

def my_cb2(p):
    my_threading_local.a = None
    return 1

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
my_cb_c = my_cb_type(my_cb)
my_cb2_c = my_cb_type(my_cb2)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db))
lib.sqlite3_create_function(my_threading_local.db, b"my_cb", 1, 0, ctypes.c_void_p(), my_cb_c, None, None)
lib.sqlite3_create_function(my_threading_local.db, b"my_cb2", 1, 0, ctypes.c_void_p(), my_cb2_c, None, None
