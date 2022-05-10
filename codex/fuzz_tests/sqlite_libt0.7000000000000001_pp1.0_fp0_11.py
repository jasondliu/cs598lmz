import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import datetime
import shutil
import subprocess
import locale
import sys

class Database(object):
    """
    Database class, used to store the time at which a file was copied,
    the original path, and the destination path.
    """
    def __init__(self, name, directory):
        """
        Initialize the database and the cursor.
        """
        self.DATABASE = directory + "/" + name
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.conn = sqlite3.connect(self.DATABASE)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        """
        Create the `files` table, if it doesn't already exist.
        """
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS files (
                                "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                "path" TEXT NOT
