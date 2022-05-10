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

def my_fn(a):
    return 1

sqlite3.sqlite3_initialize()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode(), ctypes.c_void_p(0))
lib.sqlite3_enable_load_extension(1)
lib.sqlite3_create_function(lib.sqlite3_db_handle(),
                            b"my_fn",
                            2,
                            None,
                            my_fn)
lib.sqlite3_set_authorizer(lib.sqlite3_db_handle(),
                           0)

my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
my_threading_local.a.enable_load_extension(True)
my_threading_local.a.create_function("my_cb", 1, my_cb)

my_threading_local.b = my
