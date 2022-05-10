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

    return 1234

gibberish_str = "asdfwerjlq3wohfiu49q823f8qefnasdnfasjd9fh9r8qrj90rnsdfa9834nase"

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    c = a.cursor()
    c.execute("select test(?, ?)", (1, 2))
    assert c.fetchall() == [(1,)]

    del a

    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    libc.malloc_trim(0)
    libc.malloc_trim(0)

    # Make sure that a second connection to the same memory database works
    # *after* the first connection is closed.
    a = sqlite3.connect(DB_URI, uri=True, factory
