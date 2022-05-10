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

assert sqlite3.connect(DB_URI, uri=True).execute("select test(?, ?)", (1, 2)).fetchone()[0] == 1

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.sqlite3_enable_shared_cache(1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_threadsafe()
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_create_collation("test", 1, my_cb)

assert sqlite3.connect(DB_URI, uri=True).execute("select test(?, ?)", (1, 2)).fetchone()[0] == 1

libc.sqlite3_enable_shared_cache(0)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 0)
sqlite3.sqlite3_shutdown()

assert sqlite3.connect(DB_URI
