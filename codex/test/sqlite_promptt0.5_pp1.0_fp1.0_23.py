import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class _PySQLite_Connection(object):
    """
    This class represents a single connection to a SQLite database.
    """
    def __init__(self, filename, flags, vfs):
        """
        Constructor.

        @param filename: The name of the database file.
        @type filename: C{str}
        @param flags: The flags to use when opening the database file.
        @type flags: C{int}
        @param vfs: The name of the VFS to use.
        @type vfs: C{str}
        """
        self._filename = filename
        self._flags = flags
        self._vfs = vfs
        self._open()

    def _open(self):
        """
        Open the database connection.
        """
