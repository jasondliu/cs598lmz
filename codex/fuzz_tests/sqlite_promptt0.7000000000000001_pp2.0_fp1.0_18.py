import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('/home/kali/Documents/logs/test.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS log (
id INTEGER PRIMARY KEY , 
timestamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
action VARCHAR(100) NOT NULL,
description VARCHAR(100) NOT NULL,
ip VARCHAR(50) NOT NULL)''')

# Save (commit) the changes
conn.commit()
print("Database created successfully")

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
print("Connection closed successfully")

# import gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk

# class MyWindow(Gtk.Window):

#     def __init__(self):
