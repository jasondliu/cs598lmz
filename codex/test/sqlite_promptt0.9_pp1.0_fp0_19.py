import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.row_factory == sqlite3.Row
import tempfile
# Test .fetchone with Row
from multiprocessing import Queue

import unittest
from test.test_support import run_unittest, import_module, cpython_only

test_sqlite_needs_usocket = ctypes.util.find_library('sqlite3') and \
                            not hasattr(ctypes.pythonapi, 'PySocketModule_Init')

# Skip tests if either the _sqlite3 or the socket module is not present.
needs_sqlite_module = unittest.skipIf(sqlite3 is None, 'requires _sqlite3 module')
needs_usocket_module = unittest.skipIf(not test_sqlite_needs_usocket, 'needs both _sqlite3 and _socket modules')


