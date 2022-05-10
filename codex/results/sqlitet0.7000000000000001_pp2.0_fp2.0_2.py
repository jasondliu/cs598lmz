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

def my_cb_with_error(p):
    if my_threading_local.a is None:
        raise sqlite3.OperationalError("No connection in threading local")

    my_threading_local.a.close()

    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    my_threading_local.a = None

    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

    libc.srand(libc.time(0)) # Seed random number generator

    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("test_with_error", 1, my_cb_with_error)

    db.create_function("test", 1, my_cb)

    t = threading.Thread(target=lambda: db.execute('SELECT test(random())').fetchone())
    t.daemon = True
    t.start()

    t2 = threading
