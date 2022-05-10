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

def test_closed_cursor():
    ctypes.pythonapi._Py_Initialize()
    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.register_adapter(float, str)

    if hasattr(sqlite3, "sqlite_version_info"):
        print("sqlite", sqlite3.sqlite_version)
    else:
        print("pysqlite", sqlite3.version)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(1) # SQLITE_CONFIG_MULTITHREAD

    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_shutdown()

    lib.sqlite3_initialize()

    cb = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(my_cb)

    lib.sqlite3_open_v2(b"", ctypes.byref(ctypes.c_void
