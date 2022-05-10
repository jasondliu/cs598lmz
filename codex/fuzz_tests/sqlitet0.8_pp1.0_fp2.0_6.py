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

def my_rb(p, i, f):
    if i == 1:
        my_threading_local.a.execute("SELECT test(32, 33)")
    return 1

def my_bf(p, i):
    if i == 1:
        my_threading_local.a.commit()
        my_threading_local.a.close()
    return 1

c_cb = sqlite3.SQLITE_TRACE_STMT
c_rb = sqlite3.SQLITE_TRACE_ROW
c_bf = sqlite3.SQLITE_TRACE_CLOSE

lib = ctypes.util.find_library("sqlite3")
if lib is None:
    raise Exception("Can't find libsqlite3")

lib = ctypes.cdll.LoadLibrary(lib)

lib.sqlite3_trace_v2(None, c_cb, my_cb, None)
lib.sqlite3_trace_v2(None, c_rb, my_rb, None)
lib.sqlite3_trace_v2
