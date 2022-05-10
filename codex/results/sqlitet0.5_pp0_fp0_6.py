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

def my_thread_fn(i):
    p = ctypes.c_void_p()
    p.value = i
    my_cb(p)

def main():
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.create_function("test", 2, lambda a, b: a)
    c.execute("select test(1, 2)")
    print c.fetchone()

    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    threads = []
    for i in range(100):
        p = ctypes.c_void_p()
        p.value = i
        t = threading.Thread(target=my_thread_fn, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Check that we can still access the global connection
    c.execute("select test(1, 2)")
    print c.fetchone()


