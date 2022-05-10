import ctypes
import ctypes.util
import threading
import sqlite3
import re

"""
Adminer (formerly known as phpMinAdmin) is a full-featured MySQL management
tool written in PHP. Conversely to phpMyAdmin, it consist of a single file
ready to deploy to the target server. Adminer is available for MySQL, MariaDB,
PostgreSQL, SQLite, MS SQL, Oracle, Firebird, SimpleDB, Elasticsearch and
MongoDB.

https://www.adminer.org/
"""

RE_FUNC = re.compile('''
(?P<name>\w+)\s*\((?P<args>.*?)\)\s*$
''', re.VERBOSE)


def params(args, attach=None, builtins=None):
    """
    Return a tuple of
    (
    [list of parameter names],
    [list of parameter values],
    {
        'builtins': list of builtins,
        'attach': list of files attached to the form
    }
    )
    """
    # Avoid circular dependencies
    from config import load_settings
    settings = load_settings()

    #
