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

def test_create_function_ref_count():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(DB_URI.encode("ascii"), ctypes.byref(my_threading_local.db))
    lib.sqlite3_busy_handler(my_threading_local.db, my_cb, 0)
    lib.sqlite3_close(my_threading_local.db)

threads = [threading.Thread(target=test_create_function_ref_count) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
