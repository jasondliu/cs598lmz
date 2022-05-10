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

sqlite3.sqlite3_enable_shared_cache(1)

# sqlite3.sqlite3_open_v2("test", ctypes.byref(handle), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)

sqlite3.sqlite3_open(":memory:", ctypes.byref(handle))

sqlite3.sqlite3_create_function(handle, "my_cb", 1, 1, 0, my_cb)

sqlite3.sqlite3_exec(handle, "select test(my_cb(1), 1)", 0, 0, 0)
print my_threading_local.a
my_threading_local.a = None

sqlite3.sqlite3_close(handle)
