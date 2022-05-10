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
    sqlite3.set_autocommit(False)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.enable_callback_tracebacks(True)
    conn.set_progress_handler(my_cb, 2)
    c = conn.cursor()
    c.execute("create table t(a);")
    c.executemany("insert into t(a) values (?)", [(1,), (2,)])

    t = threading.Thread(target=lambda: c.execute("select test(a, a) from t"))
    t.daemon = True
    t.start()

    # Wait for the thread to do some work.
    while ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident),
                                                     ctypes.py_object(KeyboardInterrupt)) == 0:
        pass

    print my_threading_local

if __name__ == "__main__":
    main()
