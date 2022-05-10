import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import json
from pymouse import PyMouseEvent


class MouseEvent(PyMouseEvent):
    def __init__(self, sqlite_connection, cursor):
        PyMouseEvent.__init__(self)
        self.conn = sqlite_connection
        self.cursor = cursor

    def click(self, x, y, button, press):
        if press:
            print("click")
            self.cursor.execute("INSERT INTO clicks (x, y) VALUES (?, ?)", (x, y))
            self.conn.commit()

    def move(self, x, y):
        self.cursor.execute("INSERT INTO mouse_moves (x, y) VALUES (?, ?)", (x, y))
        self.conn.commit()

    def scroll(self, x, y, vertical, horizontal):
        self.cursor.execute("INSERT INTO scrolls (vertical, horizontal) VALUES (?, ?)", (vertical, horizontal))
        self.conn.commit()


lib = ctypes.cdll.LoadLibrary(ctypes.
