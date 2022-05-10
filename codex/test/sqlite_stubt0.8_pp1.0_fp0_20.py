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

if __name__ == "__main__":
    sqlite3.sqlite_version_info = (3,8,6,1)
    ctypes_util = ctypes.util.find_library("sqlite3")
    ctypes_sqlite = ctypes.CDLL(ctypes_util)
    ctypes_sqlite.sqlite3_config(ctypes_sqlite.SQLITE_CONFIG_MULTITHREAD)

    ctypes_sqlite.sqlite3_profile.argtypes = [ctypes_sqlite.c_void_p, ctypes_sqlite.c_void_p, ctypes_sqlite.c_char_p]
    ctypes_sqlite.sqlite3_profile.restype = ctypes.c_void_p

    ctypes_sqlite.sqlite3_profile(None, my_cb, None)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("create table t (t integer)")
