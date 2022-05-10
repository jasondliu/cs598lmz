import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')
# The database is stored in your computer’s memory, not in a file.
# create cursor to execute SQL
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
c.close()
# conn.close()
class Coroutine:
    def __init__(self, func):
        self.__func = func

    def __call__(self):
        self.__gen = self.__func()
        next(self.__gen)
        return self
