import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class SQLite3Thread(threading.Thread):
    def __init__(self, dbname):
        threading.Thread.__init__(self)
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        self.conn.execute('create table test(id integer primary key, value text)')
        self.conn.execute('insert into test(value) values(?)', ('a',))
        self.conn.execute('insert into test(value) values(?)', ('b',))
        self.conn.commit()
        self.conn.close()

    def run(self):
        conn = sqlite3.connect(self.dbname)
        for i in range(100):
            conn.execute('insert into test(value) values(?)', ('a',))
            conn.execute('insert into test(value) values(?)', ('b',))
            conn.commit()
        conn.close()

