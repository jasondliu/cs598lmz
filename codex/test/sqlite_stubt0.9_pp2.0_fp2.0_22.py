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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.enable_callback_tracebacks(True)
sqlite3.create_function("throw", 1, None)
with sqlite3.connect(DB_URI, uri=True) as a:
    a.create_collation("BINARY", lambda x, y: cmp(x.encode("utf-8"), y.encode("utf-8")))

