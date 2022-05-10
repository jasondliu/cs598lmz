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

def my_status(a):
    return 1

def my_trace(a):
    return 1

sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.conn), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)
sqlite3.sqlite3_create_function(my_threading_local.conn, "test", 2, 0, None, my_cb, None, None)
sqlite3.sqlite3_trace(my_threading_local.conn, my_trace, None)
sqlite3.sqlite3_progress_handler(my_threading_local.conn, 100, my_status, None)

def test_function():
    assert(my_threading_local.a.execute("select test(1, 2)").fetchone()[0] == 1)

for i in range(100):
    test_function()
