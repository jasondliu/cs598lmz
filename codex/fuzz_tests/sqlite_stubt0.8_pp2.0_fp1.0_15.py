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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_HEAP, ctypes.c_int(500), ctypes.c_int(2), ctypes.c_int(1))
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_enable_shared_cache(1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs_find("unix-none"), 1)

my_threading_local.b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
sqlite3.sqlite3_wal_autocheckpoint(my_threading_local.b, 1)
my_threading_local.c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
sqlite3.sqlite3
