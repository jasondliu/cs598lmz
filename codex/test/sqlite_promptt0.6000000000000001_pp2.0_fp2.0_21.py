import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
try:
    sqlite3.connect(':memory:')
except:
    raise ImportError('sqlite3 is not available')

try:
    import pysqlite2.dbapi2
except ImportError:
    pysqlite2 = None

if pysqlite2:
    # Test pysqlite2.connect()
    try:
        pysqlite2.connect(':memory:')
    except:
        pysqlite2 = None

import time

# The following code is based on the following article:
# http://www.nehalemlabs.net/prototype/blog/2009/01/14/porting-sqlite-to-use-pythons-sqlite3-module/

def _sqlite_version_check():
    """
    Check that the sqlite library is recent enough.
    """
    return sqlite3.sqlite_version_info >= (3, 3, 8)

