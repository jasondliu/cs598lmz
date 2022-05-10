import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

HAVE_SHARED_MEMORY_SUPPORT = False

#
# sqlite3.connect():
#
#  file:memory:?cache=shared
#
#  file:name_of_file
#
#  To open a database in the file "mydb.db":
#    sqlite3.connect("file:mydb.db")
#
#  To open a temporary database held in memory:
#    sqlite3.connect(":memory:")
#
#  To open a temporary database in a file:
#    sqlite3.connect("file:")
#
#  To open a database in the file "mydb.db" using a URI:
#    sqlite3.connect("file:/home/me/mydb.db")
#
#  To open a database in the file "mydb.db" using a Windows path:
#    sqlite3.connect("file:///C:/Documents%20and%20Settings/me/mydb.db")
#
#  To open a database in the
