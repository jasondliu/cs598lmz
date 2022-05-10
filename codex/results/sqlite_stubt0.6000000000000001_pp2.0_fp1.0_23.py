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
    # this is a workaround for memory leak in SQLite3
    # http://bugs.python.org/issue15113
    my_threading_local.a.close()
    del my_threading_local.a
    return 0

def foo():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_thread_cleanup()
    lib.sqlite3_config(ctypes.c_int(0x00080000), my_cb, my_cb2)
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.close()

threads = []
for i in range(0, 10):
    t = threading.Thread(target=foo)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
</code>


A:

This is a bug in the sqlite3 module, it appears to
