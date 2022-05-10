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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db_p))
sqlite3.sqlite3_busy_handler(my_threading_local.db_p.value,
                             sqlite3.sqlite3_busy_handler(0, None), None)
sqlite3.sqlite3_busy_timeout(my_threading_local.db_p.value, 600)
sqlite3.sqlite3_exec(my_threading_local.db_p.value, """
 create table log (id int primary key, name varchar(64)) ;
""", 0, 0, 0)

sqlite3.sqlite3_busy_handler(my_threading_local.db_p.value, my_cb, None)

my_threading_local.a.execute("INSERT INTO log VALUES (1, 'test')")
</code>
I'm using sqlite3 as a worker queue, hence the need for the busy handler.  The above code throws an error.
