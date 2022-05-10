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

if __name__ == '__main__':
    ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

    p = ctypes.c_void_p()
    sqlite3.sqlite3_open(DB_URI, ctypes.byref(p))

    sqlite3.sqlite3_busy_handler(p, my_cb, None)

    t = threading.Thread(target=lambda: sqlite3.sqlite3_exec(p, "create table t(x)", None, None, None))
    t.start()
    t.join()

    c = sqlite3.connect(DB_URI, uri=True)

    c.execute("select test(?)", (1,))
    c.execute("select test(?)", (1,))
    c.execute("select test(?)", (1,))

    print "ok"
