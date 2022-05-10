import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Globals:
    def __init__(self):
        self.db = sqlite3.connect(':memory:')
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS `fib` (
                `fib` INTEGER NOT NULL,
                `fib_inv` INTEGER NOT NULL
            );
        ''')
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS `fib_inv` (
                `fib_inv` INTEGER NOT NULL,
                `fib` INTEGER NOT NULL
            );
        ''')
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS `fib_inv2` (
                `fib_inv2` INTEGER NOT NULL,
                `fib2` INTEGER NOT NULL
            );
        ''')
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS `fib2` (
                `fib2` INTEGER NOT NULL
