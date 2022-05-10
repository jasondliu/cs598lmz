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

my_cb_ctypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_cb)
sqlite3.sqlite3_profile_v2(my_cb_ctypes, 1)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

try:
    a.execute("select test(1, 2)")
finally:
    del my_threading_local.a

# Deliberately access this and make sure it has gone.
a.execute("select test(1, 2)")
