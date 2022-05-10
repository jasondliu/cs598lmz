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

    return 10

def my_authorizer(a, b, c, d, e):
    return sqlite3.SQLITE_DENY

def my_trace(a, b, c, d):
    return

def test_threads():
    sqlite3.sqlite3_enable_shared_cache(1)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.set_authorizer(my_authorizer)
    a.set_trace_callback(my_trace)
    a.executescript("create table t1(x);")

    my_threading_local.a = a

    threads = []
    for x in xrange(4):
        t = threading.Thread(target=my_cb, args=(x,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def test_fork():
    pid =
