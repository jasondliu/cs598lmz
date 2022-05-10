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

def my_cb2(p):
    a = my_threading_local.a
    a.execute("insert into test values(1)")
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.execute("select test(1, ?)", (2,))
    return 1

if __name__ == "__main__":
    print("sqlite3 version: %s" % (sqlite3.sqlite_version,))

    sqlite3.enable_callback_tracebacks(True)

    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_trace_v2(None, 0, my_cb, None)
    libsqlite3.sqlite3_trace_v2(None, 0, my_cb2, None)
    libsqlite3.sqlite3_trace_v2(None, 0, my_cb3, None)

    c = sqlite3.connect(DB_URI, ur
