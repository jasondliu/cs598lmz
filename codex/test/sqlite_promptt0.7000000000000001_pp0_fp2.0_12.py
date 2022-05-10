import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import time
import re

class CorruptDBError(Exception):
    """
    Raised when there is an error in the database
    """
    pass

class Database(object):
    """
    Superclass for writing to and reading from SQLite3 databases
    """
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.db_name = db_name

        # Use the same row factory as csv.DictReader()
        self.db.row_factory = self._row_factory

    def _row_factory(self, cursor, row):
        """
        Maps the contents of a row to a dictionary object
        """
        d = {}

        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def _get_attr_names(self, instance):
        """
        Returns a set of the attribute names of an instance
        """
