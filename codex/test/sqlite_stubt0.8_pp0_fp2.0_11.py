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

cb_ctype = ctypes.CFUNCTYPE(ctypes.c_int)
cb_p = cb_ctype(my_cb)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('pthread'))
lib.pthread_create(None, None, cb_p, None)
