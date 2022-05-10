import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Cursor, Connection
from sqlite3 import ProgrammingError, InterfaceError
from sqlite3 import OperationalError
from collections import deque
from functools import wraps

from . import config
from . import util
from . import server
from . import app

#: Mapping of SQLite error codes to exceptions
#:
#: .. seealso::
#:     https://www.sqlite.org/rescode.html#misuse
EXCEPTIONS = {
    # SQLITE_MISUSE
    21: ProgrammingError,  # SQLITE_MISUSE
    # SQLITE_NOTFOUND
    26: ProgrammingError,  # SQLITE_NOTFOUND
    # SQLITE_ERROR
    1: ProgrammingError,
    2: InterfaceError,
    3: OperationalError,
    4: OperationalError,
    5: OperationalError,
    6: OperationalError,
    7: OperationalError,
    8: OperationalError,
    9: OperationalError,
    10: OperationalError,
    11: OperationalError,

