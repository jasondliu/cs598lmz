import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file::memory:?cache=shared", uri=True)

try:
    from sqlite3 import Connection
except ImportError:
    print("SKIP")
    raise SystemExit

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Create a DB in shared memory
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE test(id INTEGER PRIMARY KEY)")

# Find the name of the shared memory file
cursor = db.execute("PRAGMA database_list")
file_entry = [row for row in cursor if row[1] == ":memory:"][0]
shared_memory_file_name = file_entry[2]

# Function to open a connection to the database
def open_connection():
    return sqlite3.connect("file::memory:?cache=shared", uri=True)

# Function to insert into the database
def insert_into_database():
    conn = open_connection()
