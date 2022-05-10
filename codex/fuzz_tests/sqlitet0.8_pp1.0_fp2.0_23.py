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

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.trace_stop_count = 0x7FFFFFFF
    sqlite3.sqlite3_set_authorizer(my_cb)

    try:
        x = threading.Thread(target=my_cb)
        x.start()
        x.join()
    finally:
        y = my_threading_local.a
        y.__del__()

    x = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

main()
