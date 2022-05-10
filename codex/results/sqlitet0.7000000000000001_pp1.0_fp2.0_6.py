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

def main():
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_open_v2(DB_URI, ctypes.pointer(my_threading_local.a), 3, None)

    my_threading_local.a.enable_load_extension(True)
    my_threading_local.a.load_extension("./libtest.so", "sqlite3_extension_init")
    my_threading_local.a.execute("SELECT test(1, 1);")

    my_threading_local.a.close()

main()
