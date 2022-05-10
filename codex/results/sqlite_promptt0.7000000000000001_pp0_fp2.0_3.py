import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
import os
import sys
import traceback
import time

try:
    from sqlite3 import Connection as SQLiteConnectionBase
except ImportError:
    from pysqlite2.dbapi2 import Connection as SQLiteConnectionBase

try:
    import psycopg2
    import psycopg2.extensions
except ImportError:
    psycopg2 = None

try:
    import MySQLdb
except ImportError:
    MySQLdb = None

try:
    import pymysql
except ImportError:
    pymysql = None

try:
    import pymssql
except ImportError:
    pymssql = None


test_db_name = 'test.sqlite'
test_db_name2 = 'test2.sqlite'
test_db_prefix = ':memory:'
#test_db_prefix = ''

if sys.version_info[:2] < (2, 6):
    from sets import Set as set
    from sets import ImmutableSet as frozenset


