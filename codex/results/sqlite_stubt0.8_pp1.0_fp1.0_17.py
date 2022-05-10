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

def run_thread_fn(n):
    p = ctypes.c_void_p(n)
    my_cb(p)

my_threads = []
for i in range(10):
    t = threading.Thread(target=run_thread_fn, args=(i,), daemon=True)
    my_threads.append(t)
    t.start()

for t in my_threads:
    t.join()

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_shutdown()
