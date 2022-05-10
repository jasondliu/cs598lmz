import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('nzone.db', isolation_level='IMMEDIATE')
# Test sqlite3.connect('nzone.db', isolation_level='DEFERRED')
# Test sqlite3.connect('nzone.db', isolation_level='EXCLUSIVE')

# http://docs.python.org/library/sqlite3.html#creating-a-new-sqlite-database
class SQLiteConnection(object):
    def __init__(self, database):
        self._database = database
        self._lock = threading.RLock()
        self._connection = sqlite3.connect(self._database, check_same_thread=False)
        self._connection.text_factory = str
        self._connection.isolation_level = 'EXCLUSIVE'
        self._connection.execute('pragma journal_mode=memory')
        self._connection.execute('pragma synchronous=normal')
        #self._connection.execute('pragma journal_mode=wal')
        #self._connection.execute('pragma synchronous=full')
        self._connection.execute('
