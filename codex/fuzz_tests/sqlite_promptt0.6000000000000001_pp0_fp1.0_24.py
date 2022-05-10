import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect('/tmp/test.db')

# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect('/tmp/test.db')

# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect('/tmp/test.db')

# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect('/tmp/test.db')


class SQLite(object):
    """SQLite helper class.

    This class is a wrapper for the `sqlite3` module. It provides
    some convenience functions, such as a guard that acquires and
    releases the database lock for you.
    """
    def __init__(self, filename, timeout=20.0):
        """Create a new SQLite database in the file `filename`.

        If `filename` is ':memory:', then a database is created
        in memory instead.
        """

