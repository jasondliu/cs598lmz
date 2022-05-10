import ctypes
import ctypes.util
import threading
import sqlite3

class SqliteCache(threading.Thread):
    """Asynchronously writes cache data to sqlite

    cacheName is the name of our table, key value is a unique key (use a uuid or
    something)"""
    SELECT_QUERY = "SELECT value FROM %s WHERE key = ?"

    def __init__(self, cacheName, callback=None):
        super(SqliteCache, self).__init__()
        self.cacheName = cacheName
        self.conn = None
        self.queue = Queue.Queue()
        self.daemon = True
        self.callback = callback

    def run(self):
        while True:
            try:
                key, value = self.queue.get()
                self.insert(key, value)
                if self.callback:
                    self.callback.callback(key)
            except Queue.Empty:
                pass

    def insert(self, key, value):
        if self.conn is None:
            self.conn = sqlite3.connect(':memory:')
