import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# This is a py2exe work-around:
# http://www.py2exe.org/index.cgi/Py2exeAndSqlite
#
dll = ctypes.util.find_library('sqlite3')
if dll:
    ctypes.CDLL(dll)

class Global(object):
    def __init__(self):
        self.db = sqlite3.connect(':memory:')
        self.db_lock = threading.Lock()

global_instance = Global()

def get_db():
    '''returns a connection to an in-memory sqlite database,
    shared by all threads'''
    return global_instance.db

def get_db_lock():
    '''returns a threading.Lock object,
    shared by all threads'''
    return global_instance.db_lock

def init_db():
    '''initializes the database schema'''
    with get_db_lock():
        cursor = get_db().cursor()
        cursor.execute('''CREATE
