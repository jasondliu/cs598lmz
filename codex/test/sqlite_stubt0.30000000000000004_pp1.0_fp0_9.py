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

sqlite3.sqlite3_set_authorizer(my_cb)

def test_func():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("select test(1, 2)")

threads = []
for i in range(10):
    threads.append(threading.Thread(target=test_func))

for t in threads:
    t.start()

for t in threads:
    t.join()

