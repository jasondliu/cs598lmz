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

def setup():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    # the right way to register callbacks
    a.set_progress_handler(my_cb, 10)

    # the wrong way
    #a.set_progress_handler(None, 10)

def teardown():
    a = my_threading_local.a
    my_threading_local.a = None
    del a

def func():
    a = my_threading_local.a

    b = a.cursor()
    b.execute("create table test (a, b)")
    b.execute("insert into test (a, b) values ('a', 'b')")
    b.close()

    c = a.cursor()
    c.execute("select * from test")
    c.fetchone()
    c.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for i in range(10000):
        setup()
