import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a test of the sqlite3 module.  It is not intended to exercise
# all features of the module, but it does exercise a wide range of them.
# It also checks that the module plays nicely with the Python memory
# manager.

# The tests are defined in a class derived from unittest.TestCase.
# The setUp method creates a database and a table in it.  The tearDown
# method closes the database.  The tests themselves are methods of the
# class.

# The database is created in memory, so it is not persistent.  The
# tearDown method closes the database, so it is not available to other
# tests.  The tests are run in alphabetical order, so the order of the
# tests is not significant.

# The tests are run in a separate process, so they do not affect the
# interpreter process.  The tests are run in a separate thread, so they
# do not affect other threads in the interpreter process.

# The tests are run with the Python memory allocator disabled, so the
# Python memory allocator does
