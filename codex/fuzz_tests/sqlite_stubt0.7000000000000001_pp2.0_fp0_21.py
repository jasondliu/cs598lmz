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

def my_cb2(p):
    my_threading_local.a.close()

    return 1

_keyword_map = {
    "sqlite3_enable_shared_cache": sqlite3.SQLITE_ENABLE_SHARED_CACHE,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_SINGLETHREAD,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_MULTITHREAD,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_SERIALIZED,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_MALLOC,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_GETMALLOC,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_MEMSTATUS,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_SCRATCH,
    "sqlite3_config": sqlite3.SQLITE_CONFIG_PAG
