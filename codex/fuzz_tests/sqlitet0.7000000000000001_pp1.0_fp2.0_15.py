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

def my_cb_fini(p):
    print(my_threading_local.a.execute("SELECT test(1, 2)").fetchone()[0])

my_cb_c = sqlite3.register_callback(my_cb, my_cb_fini)

# Now make a thread that accesses the database with the custom callback
# running.
def my_thread(p):
    a = sqlite3.connect(DB_URI, uri=True)
    a.execute("SELECT 1").fetchone()

my_thread(None)

# Now make a thread that accesses the database but with the callback
# disabled.
def my_thread_no_cb(p):
    sqlite3.enable_callback(0)
    a = sqlite3.connect(DB_URI, uri=True)
    a.execute("SELECT 1").fetchone()
    sqlite3.enable_callback(1)

my_thread_no_cb(None)

# Now make a thread that accesses the database but with the callback
#
