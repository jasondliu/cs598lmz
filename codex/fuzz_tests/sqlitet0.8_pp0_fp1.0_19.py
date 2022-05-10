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

@atexit.register
def deregister_cb():
    sqlite3.sqlite3_enable_shared_cache(0)
    sqlite3.sqlite3_shutdown()

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_enable_shared_cache(1)

libsqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
libsqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_enable_shared_cache(1)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_open(DB_URI, uri=True)
sqlite3.sqlite3_open(DB_URI, uri=True
