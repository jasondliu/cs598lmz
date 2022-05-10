import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memory:?cache=shared")
from time import time
from datetime import datetime
import platform
from multiprocessing import Process
import time
from ctypes import *
from ctypes.util import find_library
import os
import sys

class test_sqlite3(unittest.TestCase):
    '''
    The following test cases perform various operations on a single sqlite3 database
    '''
    def setUp(self):
        '''
        Create a sqlite3 database file and open a connection
        '''
        self.db = sqlite3.connect("test_sqlite3.db")
        self.cur = self.db.cursor()

    def tearDown(self):
        '''
        Close the connection and delete the sqlite3 database file
        '''
        self.db.close()
        os.remove("test_sqlite3.db")

    def test_create_table(self):
        '''
        Create a table in the db and check if it exists
        '''
