import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# The sqlite3.connect() call opens a database.  If the database does not
# exist it is created.  The database is a file on the file system.
#
# The connect() call returns a connection object.  The connection object
# has methods to create cursors, commit transactions, rollback transactions,
# and close the database connection.
#
# The connection object has an attribute named 'cursor' which is a cursor
# object.  The cursor object has methods to execute SQL statements, fetch
# rows from the result set, and close the cursor.
#
# The cursor object has an attribute named 'description' which is a
# sequence of 7-item sequences.  Each of these sequences contains
# information describing one result column:
#
#   (name, type_code, display_size, internal_size, precision, scale, null_ok)
#
# The 'name' is a string representing the name of the column.
#
# The 'type_code' is an integer representing the type of data in the column.
#
# The 'display_size' is the normal maximum width in characters for
