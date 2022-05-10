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

my_cb_ref = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p(0)))
lib.sqlite3_busy_handler(0, my_cb_ref, 0)

# Force a GC and see that the connection is still open
import gc
gc.collect()

# Force the resulting threads to end, which should close the connection
import time
time.sleep(1)
