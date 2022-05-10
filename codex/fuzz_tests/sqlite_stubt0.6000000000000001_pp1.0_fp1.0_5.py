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

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MEMSTATUS), 0)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SINGLETHREAD))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MUTEX),
    sqlite3.sqlite3_mutex_alloc(sqlite3.SQLITE_MUTEX_RECURSIVE))
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MEMSTATUS), 1)

sqlite3.sqlite3_enable_shared_cache(1)

sqlite3.sqlite3_open_v2(":memory:", ctypes.byref
