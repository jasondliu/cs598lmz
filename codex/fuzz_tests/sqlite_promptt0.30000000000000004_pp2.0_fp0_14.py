import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class TestThread(threading.Thread):
    def __init__(self, db):
        threading.Thread.__init__(self)
        self.db = db
        self.cur = self.db.cursor()
        self.cur.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
        self.cur.execute('INSERT INTO test (name) VALUES (?)', ('test',))
        self.cur.execute('SELECT * FROM test')
        self.db.commit()
        self.cur.close()
        self.db.close()

class TestThread2(threading.Thread):
    def __init__(self, db):
        threading.Thread.__init__(self)
        self.db = db
        self.cur = self.db.cursor()
        self.cur.execute('INSERT INTO test (name) VALUES (?)', ('test2',))
        self.cur.execute('SELECT * FROM test')
        self.db.commit()
        self.cur.
