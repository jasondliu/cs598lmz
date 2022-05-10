import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

# Constants

#
# The various types of column values that we can extract.
#
SQLITE_INTEGER = 1
SQLITE_FLOAT   = 2
SQLITE_TEXT    = 3
SQLITE_BLOB    = 4
SQLITE_NULL    = 5

#
# The various types of SQL statements that we can process.
#
SQLITE_INSERT  = 18
SQLITE_UPDATE  = 23
SQLITE_DELETE  = 9

#
# The callback called by sqlite3_exec() when a row is to be returned.
#
def callback(p_data, num_cols, column_values, column_names):
    print("callback(): " + str(column_values[0]))

#
# Get the path to the sqlite3.exe file.
#
sqlite_path = ctypes.util.find_library("sqlite3")
if sqlite_path is None:
    print("Could not find the sqlite3 library.")
    exit(1)

#
# Load the sql
