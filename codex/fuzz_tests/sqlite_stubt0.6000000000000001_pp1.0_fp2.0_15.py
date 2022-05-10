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

sqlite3.sqlite3_auto_extension(ctypes.cast(my_cb, ctypes.CFUNCTYPE(ctypes.c_int)))

conn = sqlite3.connect(DB_URI, uri=True)

assert my_threading_local.a is not None
assert my_threading_local.a.execute("SELECT test(5, 6)").fetchone() == (5,)

conn.close()
