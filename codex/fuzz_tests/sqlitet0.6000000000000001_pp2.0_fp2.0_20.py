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

sqlite3.enable_shared_cache(True)
sqlite3.threadsafety = 2

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_enable_shared_cache(1)
sqlite3.sqlite_version_info

sqlite3.sqlite_version_info

sqlite3.sqlite_version_info

sqlite3.sqlite_version_info

my_cb(None)

my_threading_local.a.execute("select test(1, 2)").fetchall()
