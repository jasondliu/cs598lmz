import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
import time
import os

from . import common

# keep a global connection to the database
db = None

def connect(db_file):
    global db
    db = sqlite3.connect(db_file)
    db.row_factory = sqlite3.Row

def close():
    global db
    db.close()

def get_db():
    return db

def get_db_cursor():
    return db.cursor()

def get_db_row(cursor):
    return cursor.fetchone()

def get_db_rows(cursor):
    return cursor.fetchall()

def get_db_rows_as_dict(cursor):
    return common.rows_to_dict(cursor.fetchall())

def get_db_rows_as_dict_list(cursor):
    return common.rows_to_dict_list(cursor.fetchall())

