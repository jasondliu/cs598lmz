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


def test_callback():
    print("Testing callback")

    cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    C = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    C.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
    C.sqlite3_busy_handler(my_threading_local.db, cb, 0)
    C.sqlite3_exec(my_threading_local.db, "CREATE TABLE t1 (x)", None, None, None)

    for i in range(100):
        my_threading_local.a.execute("INSERT INTO t1 VALUES (test(?, ?))", (i, i))

    my_threading_local.a.commit()

    print("Testing callback done")


test_callback()

print("Testing threading")

for i in range(100):
    t = threading.Thread(target=test_callback)
    t
