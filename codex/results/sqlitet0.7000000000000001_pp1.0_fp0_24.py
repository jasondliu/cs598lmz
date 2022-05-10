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

def my_cb_auth(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    a.enable_load_extension(True)
    a.execute("select load_extension('sqlite3')")

    my_threading_local.a = a

    return 1

def my_auth_init(p, s):

    return 1

def _get_sqlite3_so(version):
    try:
        sqlite3_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    except OSError:
        return None

    if not hasattr(sqlite3_lib, "sqlite3_libversion_number"):
        return None

    lib_version = sqlite3_lib.sqlite3_libversion_number()

    if lib_version < version:
        return None

    sqlite
