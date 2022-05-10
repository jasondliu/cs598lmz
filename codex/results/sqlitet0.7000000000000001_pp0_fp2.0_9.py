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

libsqlite = ctypes.util.find_library('sqlite3')
assert libsqlite is not None

libsqlite = ctypes.CDLL(libsqlite)

libsqlite.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.conn),
    sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)

libsqlite.sqlite3_db_config(my_threading_local.conn, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, None)
libsqlite.sqlite3_load_extension(my_threading_local.conn, b"libsqlitefunctions", 0, ctypes.byref(my_threading_local.errmsg))
libsqlite.sqlite3_enable_load_extension(my_threading_local.conn, 1)

libsqlite.sqlite3_create_function_v2(my_threading_local
