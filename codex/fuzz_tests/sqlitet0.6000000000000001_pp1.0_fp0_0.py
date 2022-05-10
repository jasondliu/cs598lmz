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

# Add a callback to the list of callbacks to be invoked when a new connection is created
sqlite3.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db_handle), 0, None)
sqlite3.sqlite3_update_hook(my_threading_local.db_handle, my_cb, None)

# Create a second connection to the database
sqlite3.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db_handle2), 0, None)
sqlite3.sqlite3_update_hook(my_threading_local.db_handle2, my_cb, None)

# Create a third connection to the database
sqlite3.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db_handle3), 0, None)
sqlite3.sqlite3_update_hook(
