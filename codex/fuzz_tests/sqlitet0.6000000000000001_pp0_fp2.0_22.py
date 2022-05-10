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

try:
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
except OSError:
    libc = ctypes.CDLL(ctypes.util.find_library('msvcrt'), use_errno=True)

if libc.getenv("SQLITE_FORK_TEST_THREADS"):
    for i in range(20):
        MyThread().start()

sqlite3.enable_shared_cache(True)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

if libc.fork():
    b.close()

    try:
       
