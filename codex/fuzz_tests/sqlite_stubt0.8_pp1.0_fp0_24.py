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

def my_thread():
    p = sqlite3.load_shared_library(".libs/mod.so")
    sqlite3.enable_shared_cache(True)
    sqlite3.set_authorizer(my_cb, p)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

threads = []
for i in range(10):
    threads.append(threading.Thread(target=my_thread))

for t in threads:
    t.start()

for t in threads:
    t.join()
