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

    a.execute(b'SELECT test(2, 3)')
    res = a.fetchone()[0]

    return 1

def main():
    s = sqlite3.create_function('test_cb', 1, my_cb)
    s2 = sqlite3.create_function('test_cb2', 1, my_cb2)

    main_db = sqlite3.connect(DB_URI, uri=True)
    main_db.execute('CREATE TABLE test(a)')
    main_db.execute('INSERT INTO test(a) VALUES(test_cb())')
    main_db.execute('INSERT INTO test(a) VALUES(test_cb2())')

if __name__ == '__main__':
    main()
</code>
In this example I create a function (test_cb) that opens a database in the callback, creates a function in it (test) and returns <code>1</code>.
I also create a second
