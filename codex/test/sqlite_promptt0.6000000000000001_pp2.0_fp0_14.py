import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect on linux
# import MySQLdb
# import _mysql_exceptions

from . import util
from . import log
from . import config
from . import credentials
from . import __version__


def sqlite3_connect(filename):
    """Thread-safe sqlite3 connection"""
    # XXX: Use sqlite3.connect() instead of sqlite3.connect()
    # XXX: to support in-memory databases
    with threading.Lock():
        return sqlite3.connect(filename, check_same_thread=False)


class Database(object):
    """Abstract base class for database backends"""
    def __init__(self, config):
        pass

    def close(self):
        """Close the database connection"""
        pass

    def get_credentials(self, domain):
        """Returns a list of credentials"""
        raise NotImplementedError

    def set_credentials(self, domain, username, password):
        """Sets credentials for the given domain"""
        raise NotImplementedError

