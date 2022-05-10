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

lib_name = ctypes.util.find_library("sqlite3")
lib_handle = ctypes.cdll.LoadLibrary(lib_name)

lib_handle.init(my_cb)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

conn.create_function("test", 2, test_fn)

assert conn.execute("SELECT test(5, 'ten')").fetchone()[0] == 5, "UDF called"
assert my_threading_local.a.execute("SELECT test(4, 'nine')").fetchone()[0] == 4, "UDF called from callback"
