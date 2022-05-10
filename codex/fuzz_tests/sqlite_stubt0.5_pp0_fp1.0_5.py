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
lib.sqlite3_config(1, my_cb, 0)

conn = sqlite3.connect(DB_URI, uri=True)

assert my_threading_local.a.execute("select test(1, 2)").fetchone()[0] == 1

del my_threading_local.a

del conn

assert my_threading_local.__dict__ == {}
