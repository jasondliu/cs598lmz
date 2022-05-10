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

sqlite3.sqlite3_shutdown()

lib = ctypes.util.find_library("sqlite3")
if not lib:
    raise Exception("unable to find the sqlite3 library")

lib = ctypes.CDLL(lib)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
sqlite3.sqlite3_initialize()

a = lib.sqlite3_open_v2(ctypes.c_char_p(":memory:"), ctypes.byref(ctypes.c_void_p()), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_FULLMUTEX, 0)

lib.sqlite3_db_config(ctypes.c_void_p(a), sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, 0)
lib.sqlite3_enable_load_extension(ctypes.
