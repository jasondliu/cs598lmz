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

def my_cb2(p):
    a = my_threading_local.a

    a.execute("SELECT test(1, 2)")
    row = a.fetchone()

    print(row)

    return 1

sqlite3.sqlite3_config(SQLITE_CONFIG_SERIALIZED)

sqlite3.sqlite3_config(SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_config(SQLITE_CONFIG_MEMSTATUS, 0)

sqlite3.sqlite3_initialize()

try:
    sqlite3.sqlite3_config(SQLITE_CONFIG_LOAD_EXTENSION, 1)
except sqlite3.Error:
    print("Could not enable loading of extensions")

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

lib.sqlite3_enable_load_extension(None, 1)

sqlite3.sqlite3_enable_load_extension(None, 1)
