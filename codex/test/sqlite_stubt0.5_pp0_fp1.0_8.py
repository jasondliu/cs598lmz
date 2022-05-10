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

try:
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_voidp()),
                            sqlite3.SQLITE_OPEN_READWRITE |
                            sqlite3.SQLITE_OPEN_CREATE |
                            sqlite3.SQLITE_OPEN_URI, None)
except sqlite3.OperationalError as e:
    if "file is encrypted or is not a database" in str(e):
        print("You need to compile pysqlite with SQLite >= 3.7.15")
        import sys
        sys.exit(77)
    raise

sqlite3.sqlite3_enable_load_extension(1)
sqlite3.sqlite3_load_extension("test", "sqlite3_python_init")

sqlite3.sqlite3_enable_load_extension(0)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

