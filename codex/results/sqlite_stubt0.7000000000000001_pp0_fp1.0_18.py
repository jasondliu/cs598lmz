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
    a = my_threading_local.a

    cursor = a.cursor()
    cursor.execute("SELECT test('hello', 'world')")
    print("1st result:", cursor.fetchall())

    my_threading_local.a = None
    del a

    return 1

def my_cb3(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    cursor = a.cursor()
    cursor.execute("SELECT test('hello', 'world')")
    print("2nd result:", cursor.fetchall())

    return 1

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

    lib.sqlite3_config(1, None)

    conn = lib.sqlite3_open_v
