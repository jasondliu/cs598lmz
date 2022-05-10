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

def my_step():
    pass

def my_final():
    pass

def main():
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    result = c.execute("select * from sqlite_master").fetchall()
    print(result)
    result = c.execute("select * from sqlite_master").fetchall()
    print(result)
    result = c.execute("select * from sqlite_master").fetchall()
    print(result)
    result = c.execute("select * from sqlite_master").fetchall()
    print(result)

    result = c.execute("select sum(length(name)) from sqlite_master").fetchone()
    print(result)

    result = c.execute("select * from sqlite_master").fetchall()
    print(result)

    c.commit()

    assert c.total_changes == 0

    result = c.execute("select * from sqlite_master").fetchall()
    print(result)
