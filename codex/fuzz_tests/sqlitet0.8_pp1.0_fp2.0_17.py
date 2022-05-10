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
sqlite3.set_authorizer(my_cb, int())

db = sqlite3.connect(DB_URI, uri=True)
db.execute("create table foo(id integer primary key, a integer)")
db.execute("insert into foo(id, a) values (1, test(2, 30))")
c = db.execute("select id, a from foo")
r = c.fetchone()
print(r)
