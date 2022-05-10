import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:test.db?mode=memory&cache=shared', uri=True)
import os
import sys
import time
import traceback

from . import _sqlite
from . import util

# pysqlite2/sqlite3 compatibility
try:
    from pysqlite2 import dbapi2 as sqlite
except ImportError:
    import sqlite3 as sqlite

try:
    from pysqlite2.dbapi2 import Connection as sqliteConnection
except ImportError:
    from sqlite3 import Connection as sqliteConnection

try:
    from pysqlite2.dbapi2 import Cursor as sqliteCursor
except ImportError:
    from sqlite3 import Cursor as sqliteCursor

try:
    from pysqlite2.dbapi2 import OperationalError as sqliteOperationalError
except ImportError:
    from sqlite3 import OperationalError as sqliteOperationalError

try:
    from pysqlite2.dbapi2 import ProgrammingError as sqliteProgrammingError
except ImportError:
    from sqlite
