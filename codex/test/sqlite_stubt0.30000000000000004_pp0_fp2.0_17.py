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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db), 0x00000001 | 0x00008000, None)
sqlite3.sqlite3_busy_handler(my_threading_local.db, my_cb, None)

def test_thread():
    my_threading_local.a.execute("select test(1, 2)")

threads = []

for i in range(100):
    t = threading.Thread(target=test_thread)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

my_threading_local.a.close()

sqlite3.sqlite3_close(my_threading_local.db)
