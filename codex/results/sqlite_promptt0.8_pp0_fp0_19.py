import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# Test all mode
# Test other functions (not implemented)

class TestSqlite3Module(unittest.TestCase):
    def test_connect(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        self.assertEqual(cur.fetchone()[0], sqlite3.sqlite_version)
        self.assertEqual(con.total_changes, 0)
        cur.execute("create table test(i int, s varchar(100))")
        cur.execute("insert into test(i, s) values(1, 'abc')")
        cur.execute("insert into test(i, s) values(1, 'def')")
        cur.execute("insert into test(i, s) values(2, 'ghi')")
        self.assertEqual(con.total_changes, 3)
        cur.execute("select * from test")
        self.assertEqual(cur.fetchall(), [(1, 'abc'), (1
