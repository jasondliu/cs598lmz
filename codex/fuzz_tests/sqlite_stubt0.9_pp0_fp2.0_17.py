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

def my_stop_fn():
    return True

libc = ctypes.CDLL(ctypes.util.find_library("c"))

cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
stop_fn = ctypes.CFUNCTYPE(ctypes.c_int)(my_stop_fn)

libc.tdb_run_actor(ctypes.c_char_p(DB_URI.encode("utf-8")), cb, stop_fn)
