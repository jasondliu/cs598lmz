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

def my_init(p):
    p.init_python()
    p.create_function('my_cb', 0, my_cb)
    p.execute('SELECT my_cb()')

if __name__ == '__main__':
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    libsqlite3.sqlite3_initialize()

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function('my_init', 0, my_init)
    conn.execute('SELECT my_init()')

    conn.execute('SELECT test(?,?)', (1,2))

    conn.close()

