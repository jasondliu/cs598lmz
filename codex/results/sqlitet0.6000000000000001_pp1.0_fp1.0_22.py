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
    assert a.execute("SELECT test('a', 'b');").fetchone() == ('a',)
    return 1

def my_cb3(p):
    a = my_threading_local.a
    assert a.execute("SELECT test('a', 'b');").fetchone() == ('a',)
    return 1

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(3, 1000)
    lib.sqlite3_initialize()

    p = lib.sqlite3_db_config(0, 2, 1)
    lib.sqlite3_db_config(p, 1, 1)

    thread_numbers = [4, 8, 16, 32, 64, 128]

    for thread_number in thread_numbers:
        my_threading_local.thread_number = thread_number
        my_threading
