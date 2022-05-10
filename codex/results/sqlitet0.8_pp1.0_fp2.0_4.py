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

my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

sqlite3.sqlite3_set_authorizer(my_cb_c, None)

def main():
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b.execute("create table test (a int)")
    b.execute("insert into test values (3), (4)")
    cursor = b.execute("select a from test")
    assert cursor.fetchall() == [(3,), (4,)]
    del b

main()
print("It worked!")
