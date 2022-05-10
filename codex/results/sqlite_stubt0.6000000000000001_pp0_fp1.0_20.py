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

my_cb_p = pysqlite_c.callback(my_cb)

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_config(pysqlite_c.SQLITE_CONFIG_URI, 1)
libsqlite3.sqlite3_initialize()
libsqlite3.sqlite3_config(pysqlite_c.SQLITE_CONFIG_SINGLETHREAD)
libsqlite3.sqlite3_config(pysqlite_c.SQLITE_CONFIG_MULTITHREAD)
libsqlite3.sqlite3_config(pysqlite_c.SQLITE_CONFIG_SERIALIZED)
libsqlite3.sqlite3_config(pysqlite_c.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.in_dll(libsqlite3, "sqlite3DefaultMalloc"))
libsqlite3.sqlite3_config(pysqlite_c.SQL
