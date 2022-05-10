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
    try:
        my_threading_local.a.execute("select test(1, 2)").fetchone()[0]
    finally:
        my_threading_local.a.close()
        del my_threading_local.a

# Load the library.
libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

# Call it.
libc.atexit(my_cb)

# Thread it.
for i in range(5):
    t = threading.Thread(target=my_thread)
    t.start()
    t.join()
