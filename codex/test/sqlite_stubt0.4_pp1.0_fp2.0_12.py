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

class SQLite3TestCase(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        self.db.executescript("""
            create table test (
                id integer primary key,
                parent integer references test(id),
                data text
            );

            insert into test (id, parent, data) values (1, 1, 'hello world');
            insert into test (id, parent, data) values (2, 2, 'goodbye world');
            insert into test (id, parent, data) values (3, 1, 'hello bob');
            insert into test (id, parent, data) values (4, 2, 'goodbye bob');
            insert into test (id, parent, data) values (5, 3, 'hello fred');
            insert into test (id, parent, data) values (6, 4, 'goodbye fred');
        """)

