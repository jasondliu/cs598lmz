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

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.on_create_connection(my_cb)

def test_impl():
    b = sqlite3.connect(DB_URI, uri=True)
    b.execute("select test(:a, :b)", {"a": 1, "b": 2})
    b.close()
    assert my_threading_local.a is None

for _ in range(10):
    test_impl()

print("OK")
