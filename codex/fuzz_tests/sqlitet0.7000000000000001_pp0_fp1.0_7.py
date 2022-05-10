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

def test_udf_with_multiple_connections():
    sqlite3.sqlite_udf_pkcs7_set_mode(sqlite3.SQLITE_UDF_PCKS7_RAW)
    sqlite3.sqlite_udf_enforce_limit(0)
    sqlite3.sqlite_udf_pkcs7_set_config("dummy")

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_enable_load_extension(0)
    dll.sqlite3_load_extension(b"sqlite_udf_pkcs7", b"sqlite3_udf_pkcs7_init", None)

    # N.B. using a URI for the first connection is required for the test to work
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test", 1, my_cb)

    b = sqlite3.connect
