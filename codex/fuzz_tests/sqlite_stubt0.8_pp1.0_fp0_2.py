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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC, ctypes.pythonapi.PyMem_Malloc)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOCSIZE, ctypes.pythonapi.PyMem_Malloc)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOOKASIDE, 10, 10)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, True, my_cb)
sqlite3.sqlite3_enable_shared_cache(True)

print(sqlite3.sqlite_version_info)

print(sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD))

print(sqlite3.sqlite3_threadsafe())
print(sqlite3.sqlite3_version())

with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as db:
