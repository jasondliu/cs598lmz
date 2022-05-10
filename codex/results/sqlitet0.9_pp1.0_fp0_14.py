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

lib = ctypes.CDLL(ctypes.util.find_library("SQLite.Interop"))
lib.sqlite3_open.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_char_p]

def main():
    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("another_test", 1, lambda p: 1)
    db.enable_load_extension(True)
    db.execute('select load_extension("SQLite.Interop", "sqlite3_open")')
    db.execute('select load_extension("SQLite.Interop", "sqlite3_extension_init")')
    db.enable_load_extension(False)

    c = sqlite3.connect(DB_URI, uri=False)
    # c = sqlite3.connect(":memory:")
    c.enable_load_extension(True)
    c.execute('select load_extension("SQLite.Inter
