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

ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

db.create_function("my_cb", 1, my_cb)

db.execute("SELECT my_cb(NULL)").fetchall()

db.execute("SELECT test(NULL,NULL)").fetchall()
</code>

