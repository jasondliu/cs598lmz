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

sqlite3.sqlite3_config(SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_db_config(sqlite3.sqlite3_db_handle_obsolete(sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(sqlite3.pointer()), 1, None)), SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1)
sqlite3.sqlite3_enable_load_extension(sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(sqlite3.pointer()), 1, None), 1)
lib = ctypes.util.find_library("sqlite3")

if lib is None:
    raise Exception("sqlite3 library is not found!")
else:
    sqlite3 = ctypes.CDLL(lib)

conn = sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(sqlite3.pointer()), 1 | 4, None)

sqlite3.
