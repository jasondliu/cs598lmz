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

def run_test(libpq):
    libpq.PQregisterThreadLock(my_cb)
    libpq.PQinitOpenSSL(0, 0)
    conn = libpq.PQconnectdb("dbname=test")
    assert libpq.PQstatus(conn) == libpq.CONNECTION_OK

    res = libpq.PQexec(conn, "select test('foo', 'bar');")
    assert libpq.PQresultStatus(res) == libpq.PGRES_TUPLES_OK
    assert libpq.PQgetvalue(res, 0, 0) == b"foo"

    libpq.PQclear(res)
    libpq.PQfinish(conn)

    for i in range(10):
        res = libpq.PQexec(conn, "select test('foo', 'bar');")
        libpq.PQclear(res)
        libpq.PQfinish(conn)

    del my_threading_local.a


