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
    for i in xrange(100):
        with my_threading_local.a, my_threading_local.a.cursor() as c:
            c.execute("SELECT test(?,?)", (18, 19))

    return 1

sqlite3.enable_callback_tracebacks(True)
sqlite3.set_trace_callback(my_cb)

tkinter.test()

for _ in xrange(2):
    t = threading.Thread(target=my_thread)
    t.start()
    t.join()

my_cb(None)
