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

def my_cb2(p):
    # This opens the connection too late, SQLite will have already
    # closed the statement by then.
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.a = a

    return 1

class TestDestroy(tests.IOTest):
    # Testing that SQLite connections are not left dangling in threads
    # created by pysqlite.
    def setUp(self):
        tests.IOTest.setUp(self)
        self.db = sqlite3.connect(DB_URI, uri=True)
        self.db.executescript("""
            create table test (
                id    integer primary key,
                value varchar,
                b     blob
            );
        """)

    def tearDown(self):
        self.db.close()
        tests.IOTest.tearDown(self)

    def GetSQLiteModule(self):
        # The dlopen implementation below doesn't work on OS X

