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
    a = my_threading_local.a
    assert a.execute("select test(?, ?)", (5, 6)).fetchone()[0] == 5
    return 1

def my_cb3(p):
    a = my_threading_local.a
    assert a.execute("select test(?, ?)", (7, 8)).fetchone()[0] == 7
    return 1

class MyThread(threading.Thread):
    def run(self, cb, *args):
        cb(*args)

def main():
    cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    cb2 = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb2)
    cb3 = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb3)

    lib = ctypes.CDLL(ctypes.util.find_library("pthread"))

    t1 = MyThread()
    t2
