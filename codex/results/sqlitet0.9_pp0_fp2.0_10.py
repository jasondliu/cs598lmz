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

sqlite3.register_progress_handler(1, my_cb)
conn = sqlite3.connect(DB_URI, uri=True)

def my_test():
    for x in xrange(100000):
        my_threading_local.a.execute("SELECT test(2, 3)").next()

threads = []
for x in range(30):
    threads.append(threading.Thread(target=my_test))

for x in threads:
    x.start()

for x in threads:
    x.join()
