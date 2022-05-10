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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open.restype = ctypes.c_int

p = my_cb
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(p)

@lib.sqlite3_open_v2
def sqlite3_open_v2(filename, ppDb, flags, zVfs):
    return f(None)

a = sqlite3.connect(DB_URI, uri=True)

a.close()

gc.collect()

time.sleep(1)
