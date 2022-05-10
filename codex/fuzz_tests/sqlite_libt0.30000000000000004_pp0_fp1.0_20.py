import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re
import json


class Db:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT, token TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, name TEXT, user_id INTEGER, size INTEGER, last_modified INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS file_chunks (id INTEGER PRIMARY KEY, file_id INTEGER, chunk_id INTEGER, chunk_size INTEGER, FOREIGN KEY(file_id) REFERENCES files(id))")

