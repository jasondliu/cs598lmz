import ctypes
import ctypes.util
import threading
import sqlite3
import os

class Database(object):
    def __init__(self, file):
        self.file = file
        self.conn = sqlite3.connect(self.file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `messages` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `message` TEXT, `date` TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `settings` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `key` TEXT, `value` TEXT)")
        self.conn.commit()

    def add_message(self, message):
        self.cursor.execute("INSERT INTO `messages` (`message`, `date`) VALUES (?, ?)", (message, str(datetime.now())))
        self.conn.commit()

