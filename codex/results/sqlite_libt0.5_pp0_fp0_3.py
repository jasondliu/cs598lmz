import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re

from . import lib
from . import lib_sqlite
from . import lib_sqlite_python
from . import lib_sqlite_python_ctypes
from . import lib_sqlite_python_ctypes_threading
from . import lib_sqlite_python_ctypes_multithreading
from . import lib_sqlite_python_ctypes_multiprocessing
from . import lib_sqlite_python_ctypes_multiprocessing_threading

#------------------------------------------------------------------------------

# The database filename.
DATABASE_FILE = 'test.db'

# The database table name.
DATABASE_TABLE = 'test'

# The number of times to insert into the database.
DATABASE_INSERT_COUNT = 100000

# The number of threads to use when testing threading.
THREAD_COUNT = 10

# The number of processes to use when testing multiprocessing.
PROCESS_COUNT = 10

#------------------------------------------------------------------------------

# The SQLite library.

