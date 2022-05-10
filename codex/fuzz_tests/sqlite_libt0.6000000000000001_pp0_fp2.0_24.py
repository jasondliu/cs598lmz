import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
from xlrd import open_workbook
import sys

class DbHandler:
    def __init__(self):
        self.db = sqlite3.connect('main.db')
        self.cursor = self.db.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

class DbCreator:
    def __init__(self, dbHandler):
        self.dbHandler = dbHandler
        self.cursor = self.dbHandler.get_cursor()

    def create_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS main')
        self.cursor.execute('''CREATE TABLE main (id INTEGER PRIMARY KEY, date TEXT,
                            name TEXT, phone TEXT, email TEXT,
                            category TEXT, subcategory TEXT,
                            worker TEXT, comment TEXT,
                            status TEXT, status_comment TEXT)
