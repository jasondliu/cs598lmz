import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import _sqlite
from . import _sqlite3
from . import util
from . import cache

from . import _sqlite3

_sqlite3.enable_callback_tracebacks(True)

class _SQLiteCache(cache.Cache):
    """
    A cache that uses a sqlite3 database.

    """
    def __init__(self, db_filename):
        """
        Initialize the cache.

        If the database file does not exist, it will be created.

        """
        self.db_filename = db_filename
        super(_SQLiteCache, self).__init__()

    def _connect(self):
        self._db = sqlite3.connect(self.db_filename)
        self._db.row_factory = sqlite3.Row
        self._db.text_factory = str
        self._db.execute('''
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value BLOB
            )
        ''')

        self._db
