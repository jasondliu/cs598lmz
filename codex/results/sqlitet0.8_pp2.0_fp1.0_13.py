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

try:
    sqlite3.sqlite_enable_shared_cache(1)
except Exception:
    pass

lib = ctypes.util.find_library("c")
lib = ctypes.CDLL(lib)
lib.do_something(ctypes.create_string_buffer(DB_URI), my_cb)

my_threading_local.a.cursor().execute("SELECT test(b) FROM (SELECT 1 AS b)").fetchone()
