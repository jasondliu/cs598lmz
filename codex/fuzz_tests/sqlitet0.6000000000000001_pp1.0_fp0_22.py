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
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.pthread_atfork(None, None, my_cb)
    fork()
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("select test(1,2)").fetchone()

if __name__ == "__main__":
    main()
