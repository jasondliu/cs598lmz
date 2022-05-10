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

# This is the global SQLite connection
sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.a))

# This is the global SQLite virtual table
sqlite3.sqlite3_create_module(my_threading_local.a, "test", ctypes.byref(my_threading_local.a), 0)

# This is the global SQLite virtual table connection
sqlite3.sqlite3_declare_vtab(my_threading_local.a, "CREATE TABLE test (a, b)")

# This is the global SQLite virtual table cursor
sqlite3.sqlite3_vtab_cursor(my_threading_local.a, ctypes.byref(my_threading_local.a))

sqlite3.sqlite3_create_function(my_threading_local.a, "my_cb", 1, 0, my_cb)

# This is the global SQLite prepared statement
sqlite3.sqlite3_prepare_v2(my_
