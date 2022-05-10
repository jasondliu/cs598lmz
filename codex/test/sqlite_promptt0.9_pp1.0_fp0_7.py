import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('BetsDB.db') without the get into the threading
conn = sqlite3.connect('BetsDB.db')
c = conn.cursor()
# Create table
c.execute("""CREATE TABLE bets
           (team text, opponent text, bet text, result text, score text)""")

# Insert a row of data
c.execute("INSERT INTO bets VALUES ('test', 'test2', 'test3', 'test4', 'test5')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
# dll_path = "libpysqlite.so"

# pysqlite2.load_dll(path)
# filename = "libpysqlite.so"
# lib = ctypes.cdll.LoadLibrary(filename)
# lib.sqlite3_open.restype = ctypes.c_char_p
