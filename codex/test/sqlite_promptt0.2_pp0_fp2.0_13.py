import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class TestSqlite3(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.execute('create table test(id integer primary key, name text)')
        self.db.execute('insert into test(name) values (?)', ('foo',))
        self.db.execute('insert into test(name) values (?)', ('bar',))
        self.db.execute('insert into test(name) values (?)', ('baz',))
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_select(self):
        cur = self.db.cursor()
        cur.execute('select name from test')
        self.assertEqual(cur.fetchall(), [('foo',), ('bar',), ('baz',)])
