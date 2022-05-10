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

def register_sqlite_hooks():
    sqlite3_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3_lib.sqlite3_set_authorizer(my_cb, None)


register_sqlite_hooks()

print(sqlite3.connect(DB_URI, uri=True).execute("SELECT test(1, 1)").fetchall())
