import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Create table
def create_table():
    conn = sqlite3.connect('test.db')
