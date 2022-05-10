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

if __name__ == "__main__":
    import sys
    import signal

    signal.signal(signal.SIGALRM, lambda signum, frame: sys.exit(1))
    signal.alarm(2)

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.threadsafety = 1
    sqlite3.set_authorizer(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.set_authorizer(my_cb)
    cur = conn.cursor()
    cur.execute("select test(1, 2)")
    cur.executemany('', [])
    cur.executemany('', [], my_cb)
    conn.commit()

    signal.alarm(0)
