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

def my_thread():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

    lib.sqlite3_shutdown.restype = ctypes.c_int
    lib.sqlite3_shutdown.argtypes = []
    lib.sqlite3_shutdown()

    lib.sqlite3_config(0, my_cb, 0)

    lib.sqlite3_initialize.restype = ctypes.c_int
    lib.sqlite3_initialize.argtypes = []
    lib.sqlite3_initialize()

    print(my_threading_local.a.execute("select test(1, 2);").fetchall())

def main():
    t = threading.Thread(target=my_thread)
    t.start()
    t.join()

main()
