import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

#-------------------------------------------------------------------------------
# Imports from other modules
#-------------------------------------------------------------------------------

from pysqlite2 import dbapi2 as sqlite

#-------------------------------------------------------------------------------
# Module Constants
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Module Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Module Classes
#-------------------------------------------------------------------------------

################################################################################
# class SQLite3DB
################################################################################

class SQLite3DB(object):
    """
    SQLite3DB wraps a sqlite3 database connection.
    """

    #---------------------------------------------------------------------------
    # Constants-ish
    #---------------------------------------------------------------------------

    #---------------------------------------------------------------------------
    # Methods
    #---------------------------------------------------------------------------

    def __init__(self, filename, autocommit=False):
        """
        Create a new SQLite3DB instance.
        """
        self.filename = filename
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None
        self.open()

    def __del__(self):
        """
        Delete a SQLite3DB instance.
        """
