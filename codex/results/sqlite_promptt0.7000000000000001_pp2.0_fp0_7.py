import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("cart_database.db").close()
# Test sqlite3.connect("user_database.db").close()

libc = ctypes.CDLL(ctypes.util.find_library("c"))

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.lock = threading.Lock()
        self.cartlock = threading.Lock()
        self.connection = sqlite3.connect("user_database.db")
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)''')
        self.connection.commit()
        cursor.close()

    def check_user(self):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT EXISTS(SELECT 1 FROM users WHERE username=? AND password=?)''', (self.username, self.password,))
        ret = cursor.fetchone()
        cursor.close()
        if
