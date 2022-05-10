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
    return 1

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.a),
                        sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE,
                        None)

my_threading_local.a.create_function("my_cb", 0, my_cb)
my_threading_local.a.create_function("my_cb2", 0, my_cb2)

my_threading_local.a.execute("select my_cb()")
my_threading_local.a.execute("select my_cb2()")

my_threading_local.a.close()
