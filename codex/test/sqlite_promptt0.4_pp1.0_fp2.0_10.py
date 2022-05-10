import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Create a new database
# conn = sqlite3.connect('test.db')

# Create a memory database
conn = sqlite3.connect(":memory:")
