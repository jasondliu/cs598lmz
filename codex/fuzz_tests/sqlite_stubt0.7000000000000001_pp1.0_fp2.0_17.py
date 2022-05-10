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

sqlite3.sqlite_open_v2(DB_URI, ctypes.byref(my_threading_local.a), 1 | 8, None)

sqlite3.sqlite_set_authorizer(my_threading_local.a, my_cb, None)

b = my_threading_local.a.execute("select test(1, 2) from sqlite_master")

b_result = b.fetchall()
print(b_result)
</code>
The actual code I am calling is more complicated, but I am able to replicate the problem with this simplified code. The issue is that I am unable to see the results from the query. The query actually runs, but I am unable to see the results. A call to <code>b.fetchall()</code> returns <code>[]</code>.
However, when I remove the call to <code>sqlite3.sqlite_set_authorizer()</code>, I am able to see the results of the query.
I have also tried calling <code>sqlite3.sqlite_set_authorizer()</
