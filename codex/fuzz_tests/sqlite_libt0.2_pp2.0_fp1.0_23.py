import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

#
# This is a simple example of a python script that uses the
# libpqxx C++ library to access a PostgreSQL database.
#
# The script creates a table, inserts a few rows, and then
# retrieves them.
#
# The script assumes that the database "testdb" exists, and
# that the user running the script has access to it.
#

#
# The following two lines are necessary to use the libpqxx
# library.
#
libpq = ctypes.CDLL(ctypes.util.find_library('pq'))
libpqxx = ctypes.CDLL(ctypes.util.find_library('pqxx'))

#
# The following class is a wrapper around the C++ class
# pqxx::connection.
#
class Connection(object):
    def __init__(self, conninfo):
        self.obj = libpqxx.new_pqxx_connection(conninfo)

    def __del__(self):
        libpqxx.delete_pqxx
