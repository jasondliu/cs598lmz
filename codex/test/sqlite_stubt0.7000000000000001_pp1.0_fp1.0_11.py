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

def main():
    print("ctypes.util.find_library('sqlite3')", ctypes.util.find_library('sqlite3'))
    print("ctypes.util.find_library('sqlite')", ctypes.util.find_library('sqlite'))

    for i in range(2):
        sqlite3.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.p), 253, None)
        sqlite3.sqlite3_close(my_threading_local.p)
        sqlite3.sqlite3_shutdown()

    sqlite3.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.p), 253, None)
    sqlite3.sqlite3_exec(my_threading_local.p, "CREATE TABLE foo(bar);", None, None, None)
