import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Let's start by making a database.
#
# If the database exists, we want to remove it to make sure that
# we aren't accidentally using it.
#
# SQLite doesn't support DROP DATABASE, so we'll just remove it
# from the filesystem.
try:
    os.unlink('test.db')
except OSError:
    pass

# Open the database.  sqlite3.connect() will create the database
# if it doesn't exist.
#
# sqlite3.connect() returns a Connection object.  This object
# contains methods for executing SQL statements and
# retrieving the results.

con = sqlite3.connect('test.db')

# Create a table named test with a single column of type integer.
#
# The sqlite3.Cursor object can be used to execute SQL statements
# and retrieve data.
#
# The Connection object returned by sqlite3.connect() can create
# a new cursor object using the cursor() method.

cur = con.cursor()
