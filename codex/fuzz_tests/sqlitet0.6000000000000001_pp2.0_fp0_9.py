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
        my_cb(None)

def test_function():
    cdll.LoadLibrary(ctypes.util.find_library("c"))
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.create_function("test", 2, lambda a, b: a)

    my_threading_local.b = b

    a = MyThread()
    b = MyThread()

    a.start()
    b.start()

    a.join()
    b.join()

    assert my_threading_local.a.execute("select test(1, 2)").fetchone()[0] == 1
    assert my_threading_local.b.execute("select test(1, 2)").fetchone()[0] == 1
