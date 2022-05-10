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
    del my_threading_local.a
    return 1

def my_test_fn(p):
    a = my_threading_local.a
    return a.execute("SELECT test(1, 2)").fetchone()[0]

def test_threads(lib):
    lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(2))
    lib.sqlite3_initialize()

    lib.sqlite3_thread_cleanup()

    lib.sqlite3_thread_init()

    lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(2))

    t1 = threading.Thread(target=my_cb, args=(lib,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=my_test_fn, args=(lib,))
    t2.start()
    t2.join()

    t3 = threading.Thread(target
