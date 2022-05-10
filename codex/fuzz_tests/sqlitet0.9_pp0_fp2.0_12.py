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

def test_func(count, db_uri=DB_URI):
    sqlite3.enable_callback_tracebacks(True)

    sqlite3.enable_shared_cache(True)

    con = sqlite3.connect(db_uri, uri=True, factory=deleting_conn)

    con.execute('create table test (id, data)')

    con.set_progress_handler(my_cb, 10)

    for _ in range(0, count):
        con.execute('insert into test (id, data) values (1, 1)')

    con.close()

    a = my_threading_local.a

    for x in range(0, count):
        cur = a.execute("select test(1, 1)")

        assert cur.fetchone()[0] == 1

    a.close()

class _TestConcurrency(_common.TestCase):
    def test_shared_connections(self):
        ts_count=5

        test_func(100)

        t1 = threading.Thread(target=test_
