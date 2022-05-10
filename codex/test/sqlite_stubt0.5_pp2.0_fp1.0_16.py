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

def test_init():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_shutdown()
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_initialize()
    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.threadsafety
    sqlite3.paramstyle
    sqlite3.complete_statement
    sqlite3.register_adapter(int, lambda x: x)
    sqlite3.register_adapter(float, lambda x: x)
    sqlite3.register_adapter(str, lambda x: x)
    sqlite3.register_converter("int", lambda x: 0)
    sqlite3.register_converter("float", lambda x: 0.0)
    sqlite3.register_converter("str", lambda x: "")
    sqlite3.connect(DB_URI, uri=True)
    sqlite3.connect(":memory:")

