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

sqlite3.sqlite3_initialize()

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

my_cb_type_instance = my_cb_type(my_cb)

sqlite3.sqlite3_config(
    sqlite3.SQLITE_CONFIG_URI,
    1
)

sqlite3.sqlite3_config(
    sqlite3.SQLITE_CONFIG_LOG,
    my_cb_type_instance,
    None
)

conn = sqlite3.connect(DB_URI)
conn.execute("drop table if exists test;")
conn.execute("create table test(id integer PRIMARY KEY AUTOINCREMENT);")
conn.execute("insert into test(id) values(test(1, 2));")
conn.commit()

print(conn.execute("select * from test;").fetchall())
</code>

