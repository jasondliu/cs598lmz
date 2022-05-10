import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class SQLite3(object):
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS kv(key TEXT PRIMARY KEY, value BLOB)')
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def get(self, key):
        self.cursor.execute('SELECT value FROM kv WHERE key=?', (buffer(key),))
        r = self.cursor.fetchone()
        return '' if r is None else str(r[0])

    def set(self, key, value):
        self.cursor.execute('REPLACE INTO kv VALUES (?, ?)', (buffer(key), buffer(value)))
        self.connection.commit()

