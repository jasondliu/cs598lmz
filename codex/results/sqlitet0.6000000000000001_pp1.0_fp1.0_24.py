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

def my_cb_destroy(p):
    my_threading_local.a.close()
    return 0

def main():
    sqlite3.enable_callback_tracebacks(True)

    # load the sqlite3.dll
    path = ctypes.util.find_library("sqlite3")
    if not path:
        raise Exception("Cannot find sqlite3 module")
    sqlite3.sqlite_version = path

    sqlite3.sqlite3_open(DB_URI, ctypes.byref(sqlite3.sqlite_handle))
    sqlite3.sqlite3_create_function(sqlite3.sqlite_handle, b'test', 1, 0, None, my_cb, None, None)
    sqlite3.sqlite3_create_function(sqlite3.sqlite_handle, b'test', 1, 0, None, None, None, my_cb_destroy)
    sqlite3.sqlite3_close(sqlite3.sqlite_handle)

main()
</code>

