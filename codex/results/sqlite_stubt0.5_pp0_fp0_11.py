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
    my_threading_local.a.close()
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("c"))
lib.test_init.restype = ctypes.c_int
lib.test_init.argtypes = (ctypes.c_void_p,)
lib.test_init(my_cb)
lib.test_init2.restype = ctypes.c_int
lib.test_init2.argtypes = (ctypes.c_void_p,)
lib.test_init2(my_cb2)

lib.test()
