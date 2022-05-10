import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
import _sqlite3
from test import support
import unittest

# We need to use a real file name in this test.
#
# The SQLite authors recommend that temporary database files be stored
# on the same file system as the main database in order to avoid potential
# problems with file locking.  There is also a limit on the number of
# simultaneously open file descriptors per process, so it's not a good idea
# to keep the temporary database in memory.
#
# The test suite creates a temporary directory, and this file will be
# automatically deleted when the test suite is done.
db_filename = support.TESTFN

# We want to ensure that the database is created in 8-bit mode, even
# when run under a UTF-8 locale.  The default test suite configuration
# sets the locale to UTF-8, so we need to force the default encoding
# manually.
support.import_module('locale').setlocale(support.LC_CTYPE, 'C')

# The sqlite3 library should be compiled with -DSQLITE_DE
