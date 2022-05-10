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

sqlite3.enable_callback_tracebacks(True)
sqlite3.set_authorizer(my_cb)

def my_thread_fn():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("select test(1, 2)")

threads = [threading.Thread(target=my_thread_fn) for i in range(1, 5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
