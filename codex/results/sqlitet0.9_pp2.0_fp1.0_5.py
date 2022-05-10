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

sqlite3.sqlite3_busy_handler(None, my_cb, None)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cur = conn.cursor()

cur.execute('CREATE TABLE Foo (x)')
cur.execute('INSERT INTO Foo VALUES (?)', (1,))
for _ in range(1000):
    cur.execute('SELECT test(x, ?) FROM Foo', (1,))

cur.close()
conn.close()
print(my_threading_local.a)
