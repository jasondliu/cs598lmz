import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True)

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import win32file
except ImportError:
    win32file = None

try:
    import win32con
except ImportError:
    win32con = None


class SQLiteLockException(Exception):
    pass


class SQLiteLockFile(object):
    """
    This class is a wrapper around a file object which will lock the file
    when entering a with statement and unlock the file when exiting the
    with statement.
    """

    def __init__(self, path, timeout=10.0, delay=0.05):
        """
        Initialize the lock file.

        :param path: The path to the file to lock.
        :param timeout: The number of seconds to wait for the lock to become
                        available before timing out.
        :param delay: The number of seconds to sleep between attempts to
                      acquire the lock.
        """
        self._path = path
