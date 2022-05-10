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

def printf(format, *args):
    sys.stdout.write(format % args)

if __name__ == "__main__":
    n = 10
    if len(sys.argv) > 1:
        n = int(sys.argv[1])

    sqlite3.enable_callback_tracebacks(True)

    sqlite3.sqlite3_open("test", ctypes.byref(my_threading_local.db))
    sqlite3.sqlite3_exec(my_threading_local.db, "create table abc (a)", None, None, ctypes.byref(my_threading_local.err))

    my_threading_local.stmt = ctypes.c_void_p(0)
    sqlite3.sqlite3_prepare_v2(my_threading_local.db, "select test(?, ?)", -1, ctypes.byref(my_threading_local.stmt), None)
    sqlite3.sqlite3_bind_int(my_threading_local.
