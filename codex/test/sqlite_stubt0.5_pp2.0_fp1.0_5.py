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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_enable_load_extension(None, 1)

dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
dll.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
dll.sqlite3_enable_load_extension(None, 1)
dll.sqlite3_load_extension(b"../ext/mod_spatialite.so", b"sqlite3_modspatialite_init", None)

dll.sqlite3_enable_load_extension(None, 0)

dll.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 0)

sqlite3.sqlite3_enable_load_extension(None, 0)

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 0)

