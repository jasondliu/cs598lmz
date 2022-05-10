import ctypes
import ctypes.util
import threading
import sqlite3
import time

class Storage(object):
    # This will be initialized in the run() method.
    _dbConn = None

    def __init__(self, dbFile):
        self._dbFile = dbFile
        self._dbLock = threading.RLock()

    # This method opens the database and returns the sqlite3.connection object.
    # The caller must not close this connection objct.
    def _getDBConn(self):
        with self._dbLock:
            if self._dbConn is None:
                self._dbConn = sqlite3.connect(self._dbFile)
            return self._dbConn

    # Perform a query (actually an insert) on the database.
    def _doQuery(self, query, params = None):
        with self._dbLock:
            conn = self._getDBConn()
            conn.execute(query, params)
            conn.commit()

    # Perform a query on the database that reads data.
    def _doSelect(self, query, params = None):
        with self._dbLock:
            conn
