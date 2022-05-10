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

if __name__ == '__main__':
    import sqlite3

    sqlite3.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
    sqlite3.sqlite3_db_config(sqlite3.sqlite3_db_handle(), sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, None)

    ret = ctypes.util.find_library("sqlite3")
    if ret:
        sqlite3.sqlite3_enable_load_extension(sqlite3.sqlite3_db_handle(), 1)

        path = ctypes.util.find_library("test")
        sqlite3.sqlite3_load_extension(sqlite3.sqlite3_db_handle(), path, None, ctypes.byref(ctypes.c_void_p()))

        c = sqlite3.connect(DB_URI
