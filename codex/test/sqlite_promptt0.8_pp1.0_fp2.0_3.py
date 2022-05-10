import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect.
# No error messages are printed.
import sqlite3
sqlite3.connect('mydb.db')

# Check that the sqlite3.connect() function exists in ctypes.
# No error messages are printed.
import ctypes.util
import ctypes
ctypes.util.find_library('sqlite3')
ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Test connection to a local copy of the sqlite3.dll library.
# No error messages are printed.
import ctypes.util
import ctypes
sqlite3dll = ctypes.CDLL('C:\\Users\\Gary\\AppData\\Local\\Programs\\Python\\Python37-32\\sqlite3.dll')

# Test connection to sqlite3 shared library.
# An error message is printed:
#     sqlite3.OperationalError: unable to open database file
import sqlite3
sqlite3.connect('C:\\Users\\Gary\\AppData\\Local\\Programs\\Python\\Python37-32\\mydb.db')
# Same error message with the following different
