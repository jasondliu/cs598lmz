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
    a = my_threading_local.a
    a.close()
    del my_threading_local.a
    return 1

sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
sqlite3.create_function("counter", 0, lambda: my_threading_local.x)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_shared_cache(0)
lib.sqlite3_config(3, my_cb, my_cb2)

for x in range(1, 100000):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.x = x
    print(a.execute("SELECT counter()").fetchone())
