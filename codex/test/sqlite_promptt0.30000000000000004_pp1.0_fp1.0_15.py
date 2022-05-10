import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Test(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.execute('create table test(data)')
        self.db.execute('insert into test values (?)', ('abc',))
        self.db.execute('insert into test values (?)', ('def',))
        self.db.execute('insert into test values (?)', ('ghi',))
        self.db.execute('insert into test values (?)', ('jkl',))
        self.db.execute('insert into test values (?)', ('mno',))
        self.db.execute('insert into test values (?)', ('pqr',))
        self.db.execute('insert into test values (?)', ('stu',))
        self.db.execute('insert into test values (?)', ('vwx',))
        self.db.execute('insert into test values (?)', ('yz ',))
        self.db.commit()

    def tearDown(self):
        self.db
