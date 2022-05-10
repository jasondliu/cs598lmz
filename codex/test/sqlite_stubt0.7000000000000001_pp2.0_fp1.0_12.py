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
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_LOG), my_cb, 0)

# test_fn is called after a.close(), so a.close() must not segfault
a = sqlite3.connect(DB_URI)
del a

# my_cb is called after sqlite3_shutdown(), so sqlite3_shutdown() must not segfault
sqlite3.sqlite3_shutdown()
