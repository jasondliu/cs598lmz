import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import platform

#import pdb

#pdb.set_trace()

#
# Global variables
#

#
# Global constants
#

#
# Global functions
#

#
# Classes
#

class Sqlite3:
    """
    This class is used to manage the sqlite3 database.
    """

    def __init__(self, db_name):
        """
        Initialize the object.
        """

        self.db_name = db_name
        self.db = None
        self.cursor = None

    def open(self):
        """
        Open the database.
        """

        self.db = sqlite3.connect(self.db_name)
        self.cursor = self.db.cursor()

    def close(self):
        """
        Close the database.
        """

        self.db.close()

    def execute(self, sql, args=None):
        """
        Execute the sql statement.
        """

        if args is None:
