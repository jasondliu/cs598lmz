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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))

my_threading_local.db.setAutocommit(0)

sqlite3.sqlite3_progress_handler(my_threading_local.db, 5, my_cb, None)

def test():
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("select test(1, 2)")

thread = threading.Thread(target=test)
thread.start()

thread.join()
