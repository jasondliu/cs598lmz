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


class MyThread(threading.Thread):
    def run(self):
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        a.create_function("test", 2, test_fn)
        my_threading_local.a = a


def test_function_threading():
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.create_function("test", 2, test_fn)
    my_threading_local.b = b
    threads = []
    for i in range(100):
        threads.append(MyThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def test_function_threading_lock():
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.create_function("test", 2, test_fn)
    my_threading_local.b = b

