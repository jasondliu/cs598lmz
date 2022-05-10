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

sqlite3.sqlite3_initialize()

p = ctypes.c_int(1)

sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.dbconn))

sqlite3.sqlite3_trace_v2(my_threading_local.dbconn, 0, my_cb, p)

my_threading_local.a.execute("SELECT test(1,2)").fetchall()

sqlite3.sqlite3_shutdown()
