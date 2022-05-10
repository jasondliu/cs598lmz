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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

def test_threading():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)
    lib.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))

    lib.sqlite3_initialize()

    lib.sqlite3_test_control(ctypes.c_int(1), my_cb, 0)
    lib.sqlite3_test_control(ctypes.c_int(2), my_cb_2, 0)

    for i in range(10):
        t = threading.Thread(target=lib.sqlite3_test_control, args=(ctypes.c_int(3), 0, 0))
        t.start()
        t.join()

    lib.sqlite3_shutdown()

if __name__ == "__main__":
    test_thread
