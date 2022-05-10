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

def my_cb_thread():
    my_cb(None)

def main(args):
    if len(args) > 1 and args[1] == "thread":
        my_threading_local.a = None
        t = threading.Thread(target=my_cb_thread)
        sqlite3.sqlite3_threadsafe()
        t.start()
        t.join()
        assert my_threading_local.a
    else:
        sqlite3.enable_callback_tracebacks(True)
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.create_function("testcb", 1, my_cb)
        conn.execute("SELECT testcb(1)")
        assert my_threading_local.a

if __name__ == "__main__":
    import sys
    main(sys.argv)
