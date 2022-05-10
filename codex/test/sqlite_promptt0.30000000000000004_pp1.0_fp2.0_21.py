import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

import pysqlite2.dbapi2 as sqlite

import pysqlite2.test

class SharedCacheTests(pysqlite2.test.DbTestCase):
    def setUp(self):
        self.lock = threading.Lock()
        self.con = sqlite.connect(':memory:', check_same_thread=False)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(x)')
        self.cur.execute("insert into test(x) values ('foo')")
        self.con.commit()

    def tearDown(self):
        self.con.close()

    def CheckPragma(self, pragma, expected):
        self.cur.execute('pragma %s' % pragma)
        row = self.cur.fetchone()
        self.assertEqual(row[0], expected)

