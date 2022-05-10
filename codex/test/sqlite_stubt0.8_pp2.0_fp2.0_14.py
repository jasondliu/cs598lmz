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

def my_cb2(p):
    my_threading_local.a.create_function("test2", 2, lambda a, b: a)

    return 1

def my_cb3(p):
    c = my_threading_local.a.cursor()
    c.execute("select test(1, ?)", ("abc",))
    print(c.fetchall())

    c.execute("select test2(1, ?)", ("abc",))
    print(c.fetchall())

    del my_threading_local.a

    return 1

sl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
sl.sqlite3_enable_shared_cache(1)

t = threading.Thread(target=my_cb, name="thread_1")
t.start()
t.join()

t = threading.Thread(target=my_cb2, name="thread_2")
t.start()
t.join()

