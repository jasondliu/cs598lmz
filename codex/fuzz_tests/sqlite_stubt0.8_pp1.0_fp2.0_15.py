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

def create_a(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

def do_sql(p):
    a = my_threading_local.a
    c = a.cursor()
    c.execute("select test(1, 3)")
    return c.fetchone()[0]

def my_thread_func():
    create_a(None)
    for i in range(0, 100000):
        do_sql(None)

threads = []
for i in range(0, 10):
    th = threading.Thread(target=my_thread_func)
    threads.append(th)
    th.start()

for th in threads:
    th.join()
