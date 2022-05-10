import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb?mode=memory', uri=True)
# Test sqlite3.connect('file:memdb?cache=shared', uri=True)

# Test sqlite3.connect(':memory:', uri=True)

class _TestSharedCache(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.db = sqlite3.connect(':memory:')
        self.db.execute('CREATE TABLE test(id integer primary key)')
        self.db.execute('INSERT INTO test VALUES(1)')
        self.db.commit()
        self.db.execute('INSERT INTO test VALUES(2)')
        self.db.execute('SELECT * FROM test')
        self.db.commit()
        self.db.execute('SELECT * FROM test')
        self.db.execute('SELECT * FROM test')
        self.db.execute('SELECT * FROM test')

