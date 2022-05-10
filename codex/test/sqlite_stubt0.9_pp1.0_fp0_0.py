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
    
print("creating shared cache")
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
conn = sqlite3.connect(DB_URI, uri=True)

lib.sqlite3_enable_shared_cache(1)
lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)

lib.sqlite3_initialize()

lib.sqlite3_open_v2(b"testdb", ctypes.byref(p), lib.SQLITE_OPEN_READWRITE | lib.SQLITE_OPEN_URI, c_void_p(0))

print("loading extensions")
lib.sqlite3_load_extension(p, b":memory:", b"enumfile\x00foo\x00", c_void_p(0))
