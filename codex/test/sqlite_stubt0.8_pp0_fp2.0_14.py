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

cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

try:
    sqlite3.enable_shared_cache(True)
except AttributeError:
    print("SKIP")
    raise SystemExit

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(3, cb, None)

db = sqlite3.connect(DB_URI, uri=True)

# This would segfault if the bug is still present
db.execute("select test(1, 2)")

# This would fail without the workaround in enable_shared_cache()
