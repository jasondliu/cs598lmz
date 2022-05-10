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

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

odb = ctypes.cdll.LoadLibrary(ctypes.util.find_library("odb"))

odb.thread_cb_c.argtypes = [my_cb_p, ctypes.c_void_p]
odb.thread_cb_c(my_cb_p, None)

# Now x should leak...
assert my_threading_local.a
