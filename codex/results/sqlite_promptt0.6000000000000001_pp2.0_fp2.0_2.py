import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memory:?cache=shared')

from sqlite3 import dbapi2 as sqlite


def sqlite3_version_info():
    """Return sqlite3 version as an integer.

    10700 is 3.7.0, for example.

    """
    try:
        return sqlite.sqlite_version_info
    except AttributeError:
        # Stale pysqlite version, return something that's
        # greater than the version we support.
        return 200000


def sqlite3_version():
    """Return sqlite3 version as a string."""
    try:
        return sqlite.sqlite_version
    except AttributeError:
        # Stale pysqlite version, return something that's
        # greater than the version we support.
        return '99.99.99'


def sqlite3_thread_cleanup():
    """Cleanup sqlite3 threading resources.

    This function exists to workaround the lack of a threading cleanup
    function in older pysqlite.
