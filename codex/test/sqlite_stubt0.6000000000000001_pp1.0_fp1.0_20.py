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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

libsqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

libsqlite3.sqlite3_db_config(0, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1)

libsqlite3.sqlite3_enable_load_extension(0, 1)

libsqlite3.sqlite3_load_extension("extension-functions.so", "sqlite3_extension_init", 0)

libsqlite3.sqlite3_enable_load_extension(0, 0)

libsqlite3.sqlite3_db_config(0, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 0)

