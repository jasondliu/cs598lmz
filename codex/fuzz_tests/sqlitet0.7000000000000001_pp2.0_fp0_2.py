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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC, None)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.from_address(id(ctypes.string_at)))
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MEMSTATUS, True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SCRATCH, None)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_PAGECACHE, None)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_HEAP, None, 0, 0)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOOKASIDE, 128, 128)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_PCACHE, None)
sqlite3.sqlite3
