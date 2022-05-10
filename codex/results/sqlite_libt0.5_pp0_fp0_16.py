import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import configparser

# This is a class to wrap the sqlite3 database
# It will allow us to use the database in an object oriented manner
class DB:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.connection = None
        self.cursor = None
        self.open()

    def open(self):
        self.connection = sqlite3.connect(self.dbfile)
        self.cursor = self.connection.cursor()
        return self.cursor

    def execute(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()

# This is a class to wrap the libusb functions
# This will allow us to use the libusb functions in an object oriented manner
class USB:
    def __init__(self):
        # This is the vendor id and product id of the device we want to communicate with
        self.vendor = 0x04
