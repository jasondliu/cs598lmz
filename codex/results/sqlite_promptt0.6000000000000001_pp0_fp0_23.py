import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

import time
import random

def main():
  print "Test sqlite3.connect()"
  print "--"
  print "-- Before test"
  print "--"
  print "-- sqlite3.threadsafety() is:", sqlite3.threadsafety()
  print "-- sqlite3.version is:", sqlite3.version
  print "-- sqlite3.sqlite_version is:", sqlite3.sqlite_version
  print "-- sqlite3.PARSE_DECLTYPES is:", sqlite3.PARSE_DECLTYPES
  print "-- sqlite3.PARSE_COLNAMES is:", sqlite3.PARSE_COLNAMES
  print "--"
  print "-- Start test"
  print "--"

  db_filename = ':memory:'
  print "-- Open database in memory"
  db = sqlite3.connect(db_filename)
  print "-- db is:", db
  print "-- db.threadsafety is:", db.threadsafety
  print "-- db
