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
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(lambda x: 0)
    test_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    test_lib.sqlite3_open_v2(b':memory:', ctypes.byref(my_threading_local.db),
                             sqlite3.SQLITE_OPEN_READWRITE
                             | sqlite3.SQLITE_OPEN_CREATE,
                             0)
    test_lib.sqlite3_busy_handler(my_threading_local.db, my_cb, 0)
    my_threading_local.a.execute('PRAGMA authorizer = off')
    c = my_threading_local.a.cursor()
    c.execute('select test(1,2), test(1,2), 1;')
    print(c.fetchone())
    c.execute('select test(1,2), test
