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

def my_destructor(p):
    my_threading_local.a.close()
    my_threading_local.a = None

def test_udf():
    my_threading_local.a = None
    sqlite3.enable_shared_cache(True)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_collation("RANK", 1, lambda s1, s2: 0)
    sqlite3.enable_shared_cache(False)
    cdll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    cdll.sqlite3_set_authorizer(conn, 3)
    cdll.sqlite3_set_authorizer(conn, 0)
    sqlite3.threadsafety
    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    conn.threadsafety
    conn.sqlite_version
    conn.sqlite_version_info
    sqlite3.PARSE
