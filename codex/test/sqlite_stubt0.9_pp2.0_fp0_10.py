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

sqlite_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
sqlite_open = sqlite3.sqlite_api.open
sqlite_open.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
sqlite_open.restype = ctypes.c_int

for i in range(5):
    sqlite_open(DB_URI.encode(), sqlite_cb(None))
    del my_threading_local.a
