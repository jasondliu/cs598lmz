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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_db_config(0, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1)
lib.sqlite3_enable_load_extension(0, 1)
lib.sqlite3_open(0, DB_URI.encode("utf-8"), 0)

lib.sqlite3_create_function(0, b"test", 2, 0, 0, ctypes.cast(test_fn, ctypes.c_void_p))

lib.sqlite3_load_extension(0, 0, 0)

threading.Thread(target=my_cb, kwargs={}).start()

print(my_threading_local.a)
