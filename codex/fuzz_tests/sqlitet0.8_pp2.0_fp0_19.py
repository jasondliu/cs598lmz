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

# Callback to test multi-threading requirements of sqlite
sqlite3.sqlite3_set_authorizer(my_cb, None)

def test_module_init_args():
    assert_equal(sqlite3.threadsafety, 1)

def test_version():
    assert isinstance(sqlite3.sqlite_version, str)
    assert isinstance(sqlite3.version, str)
    assert isinstance(sqlite3.sqlite_version_info, tuple)
    assert isinstance(sqlite3.version_info, tuple)

def test_connect():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    curs = conn.cursor()
    curs.execute("create table test(x integer primary key, y, z);")
    curs.execute("insert into test(y, z) values (?, ?);", (1, 2))
    curs.close()
    conn.commit()
    conn.close()
    assert my_threading_local.a != None
    del
