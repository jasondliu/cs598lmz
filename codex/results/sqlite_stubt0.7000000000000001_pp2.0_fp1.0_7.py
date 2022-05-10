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

sqlite3.enable_callback_tracebacks(True)

sqlite3.set_authorizer(my_cb)

def test_fn(a, b):
    return a

my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

my_threading_local.a.create_function("test", 2, test_fn)

my_threading_local.a.execute("CREATE TABLE test(a)")
my_threading_local.a.execute("INSERT INTO test(a) VALUES(1)")

print("before test")

my_threading_local.a.execute("SELECT test(a, ?) FROM test", (1,))

print("after test")

my_threading_local.a.commit()

print("after commit")
