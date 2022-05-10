import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Can be used with any database that has a database-specific module.
# See http://docs.python.org/library/sqlite3.html
# or http://docs.python.org/library/sqlite3.html

# This example uses the Python sqlite3 module
# See http://docs.python.org/library/sqlite3.html

# To use this module, import it and call its run(args) function
# with the args passed to this script, then use the database connection
# returned.

# So, to run a query, you can do something like this:
#   import sqlite3
#   import database_lck
#   import sys
#   conn = database_lck.run(sys.argv)
#   cur = conn.cursor()
#   cur.execute("SELECT * FROM foo")
#   print cur.fetchall()

# This module will automatically create the database if it does not exist.
# You probably want to add some data to it first.

# This module will create and hold a lock file with the database
