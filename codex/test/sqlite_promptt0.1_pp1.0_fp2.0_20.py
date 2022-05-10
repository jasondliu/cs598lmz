import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a test of the sqlite3 module.  It is not a complete test, but
# it does exercise the majority of the module API.

# The tests are run in a separate process to allow repeated tests runs
# to be performed.  This is necessary as sqlite3.connect() does not
# allow a database connection to be opened on an in-memory database
# more than once within a single process.

# The tests assume the existence of a table 't1' in the 'main' database.
# The table is created as follows:
#
# CREATE TABLE t1(a, b);
# INSERT INTO t1 VALUES(1, 2);
# INSERT INTO t1 VALUES(3, 4);

# The tests also assume the existence of a table 't2' in the 'temp'
# database.  The table is created as follows:
#
# CREATE TEMP TABLE t2(a, b);
# INSERT INTO t2 VALUES(1, 2);
# INSERT INTO t2 VALUES(3, 4);
