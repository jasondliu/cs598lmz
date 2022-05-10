import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import base, file_io

def get_database():
    """Gets a handle to the database, and creates one if it doesn't exist"""
    filename = os.getenv('APPDATA') + '\NeoSearch'
    if not os.path.exists(filename):
        os.mkdir(filename)
    filename = filename + '\NeoSearch.db'
    return sqlite3.connect(filename)

def close_database(database):
    """Closes the connection to the database
    """
    database.close()

def search_database(search_string, database=None, start=0, length=0):
    """Searches the database based on the search_string"""
    search_string = '%' + search_string + '%'
    if database == None:
        database = get_database()
    cursor = database.cursor()
    if length == 0:
        cursor.execute('SELECT * FROM files WHERE name LIKE ? ' +
                      'OR name LIKE ? OR name LIKE ? ESCAPE "\" ' +
                      'OR name LIKE ?
