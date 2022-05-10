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

def my_ext_init(p):
    my_cb(p)
    return 1

sqlite3.sqlite3_enable_shared_cache(0)

try:
    sqlite3.sqlite3_enable_load_extension(1)
except AttributeError, e:
    print "SKIP", e
    raise SystemExit

sqlite3.sqlite3_initialize()

def test_load(lib, fnc):
    a = sqlite3.connect(":memory:")
    a.create_function("sqlite3_extension_init", 0, fnc)
    a.execute("SELECT sqlite3_extension_init()")
    if lib:
        fn = ctypes.util.find_library(lib)
        if not fn:
            fn = lib
        a.load_extension(fn)
    my_threading_local.a.close()
    del my_threading_local.a

try:
    test_load("pysqlite2", sqlite3._sqlite.sqlite3
