import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('database.db')

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
        self.connection.commit()

    def register_user(self, username, password):
        self.cursor.execute('INSERT INTO users(username, password) VALUES(?, ?)', (username, password))
        self.connection.commit()

    def login_user(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        self.connection.commit()
        return self.cursor.fetchone()

    def get_user_id(self, username):
        self.cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        self.connection.commit()

