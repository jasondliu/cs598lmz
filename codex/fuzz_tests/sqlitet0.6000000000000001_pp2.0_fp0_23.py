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

my_cb_p = sqlite3.free_functions.sqlite3_progress_handler_ptr(my_cb)

class MyThread(threading.Thread):
    def run(self):
        my_threading_local.a.execute("select test(?, ?)", (5, 10))

def test_thread():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_progress_handler(my_cb_p, 1, 1)

    threads = []
    for i in range(10):
        threads.append(MyThread())

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("test_thread()", setup="from __main__ import test_thread", number=1))
