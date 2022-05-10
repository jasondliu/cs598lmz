import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# This is a test of the sqlite3 module.  It is not intended to exercise
# all features of the module, nor is it intended to exercise the database
# engine itself.  It uses a database created by the SQLite authors to test
# the SQLite library.

# The database used for testing, "test.db", is a copy of test.c in the
# SQLite distribution.  The SQLite authors have kindly given permission
# to use this file to test the sqlite3 module.  The file itself is not
# covered by the Python license.

# The test.db file contains a database with a single table, t1, and a
# single index, i1.  The schema for the database is:
#
#   CREATE TABLE t1(a,b);
#   CREATE INDEX i1 ON t1(a);
#
# The database contains exactly 20 rows.  The content of each row is
# (a, b) where a is the ASCII representation of the rowid for the row
# and b is the ASCII
