import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() on all supported platforms.
# Test database file is created when it doesn't exist,
# and can be opened when it already exists.
# Test user can open database file with various options:
# read, read/write and read/write/create.
# The test database is deleted after the test.

# open file with read-only permission
# open file with read-write permission
# open file with read-write/create permission

# check if database exists
def does_db_exist(db_file):
    return os.path.isfile(db_file)

# create database
def create_db(db_file, table_name, column_name):
    if does_db_exist(db_file):
        return
    conn = sqlite3.connect(db_file)
    conn.execute('''CREATE TABLE %s
        (%s TEXT NOT NULL);''' % (table_name, column_name))
    conn.commit()
    conn.close()

# open database with flag=None
def open_db_read(db_file, table_name, column_
