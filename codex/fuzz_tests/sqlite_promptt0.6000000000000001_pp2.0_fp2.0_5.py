import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('database.db')
import os
import sys

# test
# import time
# import random

# ------------------------------
# ------------------------------
# ------------------------------


class SimpleGUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("SimpleGUI")
        self.root.geometry("900x600+0+0")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self._close)
        self.root.bind("<Escape>", self._close)

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''create table if not exists 
                            staff(id integer primary key autoincrement, 
                            name text, 
                            age integer, 
                            address text, 
                            salary real)''')
        self.conn.commit()

        # test
        # self.cursor.execute('insert
