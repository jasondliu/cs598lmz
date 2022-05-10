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
    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("my_cb", 0, my_cb)
    db.execute("SELECT my_cb()")

    try:
        db.execute("SELECT test(1,2)")
    except Exception as e:
        print(e)
        print(repr(e))

    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.prctl(1, 15)

    time.sleep(2)

    try:
        # test function from my_cb should no longer be available.
        db.execute("SELECT test(1,2)")
    except Exception as e:
        print(e)
        print(repr(e))

if __name__ == '__main__':
    main()
