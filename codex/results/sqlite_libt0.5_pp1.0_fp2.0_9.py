import ctypes
import ctypes.util
import threading
import sqlite3

from . import common
from .common import *

class SQLite3Connection(Connection):
    """
    This class implements a connection to an SQLite3 database.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None
        self.cursor = None
        self.cursor_lock = threading.Lock()
        self.username = 'root'

    def _open(self):
        """
        Internal method used to open a connection to the database.
        """
        if self.conn is not None:
            raise DatabaseError('Connection is already open')
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def _close(self):
        """
        Internal method used to close the connection to the database.
        """
        if self.conn is None:
            raise DatabaseError('Connection is not open')
        self.conn.close()
        self.conn = None
        self.
