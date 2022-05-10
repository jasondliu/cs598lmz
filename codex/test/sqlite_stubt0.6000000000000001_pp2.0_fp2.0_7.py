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
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MEMSTATUS, 0))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SCRATCH, None, 100, 500, 0))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOOKASIDE, 100, 500))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_PCACHE, None, 1, 1, 1))
print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_PAGECACHE, None, 1000, 1))
