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
    del my_threading_local.a
    a.close()

    return 1

def my_cb3(p):
    print "Step ones"
    return 1

def my_cb4(p):
    print "Step twos"
    return 1

# GIL lock that works with C and Python
g_lock = threading.RLock()

# Extra step to initialize the lock
g_lock.acquire()
g_lock.release()

class counter(object):
    def __init__(self, initial=0):
        self.counter = initial
        self.lock = threading.Lock()

    def inc(self):
        self.counter += 1

    def inc_result(self):
        with self.lock:
            self.counter += 1
            return self.counter

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self.counter = counter()
