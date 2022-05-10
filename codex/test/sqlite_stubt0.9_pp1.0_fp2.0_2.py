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

def fetch_cb(a):
    return my_threading_local.a

def closed_cb(a):
    pass

# can be run multiple times:
# - first time connects to the same db, but throws error since the function is not
#   registered with the 2nd connection
# - second time connects to the same db with the function registered
# - later times always succeed
