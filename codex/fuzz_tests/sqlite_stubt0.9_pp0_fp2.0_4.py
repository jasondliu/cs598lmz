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

def call(n):
    for i in range(n):
        libc.sqlite3_user_mode_auth(my_cb)

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.sqlite3_user_mode_auth.argtypes = (ctypes.c_void_p,)
libc.sqlite3_user_mode_auth.restype = ctypes.c_int

threads = []
for i in range(1000):
    t = threading.Thread(target=call, args=(100,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
</code>
Demo: https://repl.it/repls/BabyishScalyServerprogramming#main.py
OS: Ubuntu 18.04
Pypy: 7.1.1
SQLite: 3.26.0

