import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')

import logging
logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
# General
#------------------------------------------------------------------------------

def open_sqlite3(db_path):
    """
    Open an sqlite3 database.
    """
    return sqlite3.connect(db_path)

def get_db_path(dir_path, db_name):
    """
    Return the path of a database.
    """
    return os.path.join(dir_path, db_name)

def get_db_path_in(dir_path):
    """
    Return the path of a database in a directory.
    """
    return os.path.join(dir_path, 'db.sqlite')

def get_db_path_in_dir(dir_path):
    """
    Return the path of a database in a directory.
    """
    return os.path.join(dir_path, 'db.sqlite')

