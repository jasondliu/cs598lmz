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
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.b = a
    return 1

class SQLiteTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()

    def tearDown(self):
        self.cur.close()
        self.db.close()

    def CheckSchema(self, conn):
        cu = conn.cursor()
        schema_result = cu.execute(
            "SELECT sql FROM sqlite_master "
            "WHERE type='table' AND name=:name",
            {"name": "boing"})
        schema_sql = schema_result.fetchone()[0]
        self.assertEqual(schema_sql.lower(),
            'create table boing (x)')

    def
