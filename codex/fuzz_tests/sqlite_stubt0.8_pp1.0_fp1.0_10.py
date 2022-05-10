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
    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.db), 0, None)
    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.sqlite3_db_config(my_threading_local.db, sqlite3.SQLITE_DBCONFIG_LOOKASIDE, 0, 15, 1)

    while True:
        sqlite3.sqlite3_db_config(my_threading_local.db, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, None)
        sqlite3.sqlite3_load_extension(my_threading_local.db, ctypes.util.find_library("test"), None, ctypes.byref(my_threading_local.cb))

        my_threading_local.cb = sqlite3.sqlite3_callback_function(my_cb)

if __name__ == '__main__':
    main()
