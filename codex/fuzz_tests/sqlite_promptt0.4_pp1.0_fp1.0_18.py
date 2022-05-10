import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/test.db')

class Db(object):
    def __init__(self):
        self._db = sqlite3.connect('/tmp/test.db')
        self._cursor = self._db.cursor()
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS test
                            (id INTEGER PRIMARY KEY, name TEXT,
                             address TEXT, phone TEXT)''')
        self._db.commit()
        self._lock = threading.Lock()

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self._lock.release()
        #self._db.close()

    def insert(self, name, address, phone):
        self._cursor.execute('''INSERT INTO test(name, address, phone)
                            VALUES(?, ?, ?)''', (name, address, phone))
        self._db.commit()


