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
sqlite3.sqlite3_config(CTYPE_CONST(sqlite3.SQLITE_CONFIG_SINGLETHREAD), 0)
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_vfs_register(CTYPE_PTR(sqlite3.sqlite3_vfs), 1)
sqlite3.sqlite3_open_v2("test.db", PTR_PTR(sqlite3.sqlite3), CTYPE_CONST(sqlite3.SQLITE_OPEN_URI), "unix-none", 0)

sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_config(CTYPE_CONST(sqlite3.SQLITE_CONFIG_SINGLETHREAD), 1)
sqlite3.sqlite3_initialize()

sqlite3.sqlite3_vfs_register(CTYPE_PTR(sqlite3.sqlite3_vfs), 1)
sqlite3
