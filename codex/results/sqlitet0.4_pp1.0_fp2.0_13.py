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

def test_sqlite_threading():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_config(1, my_cb, None)
    lib.sqlite3_initialize()

    def fn():
        a = sqlite3.connect(DB_URI, uri=True)
        a.execute("select test(1, 2)")
        a.close()

    threads = [threading.Thread(target=fn) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    lib.sqlite3_shutdown()

if __name__ == "__main__":
    test_sqlite_threading()
