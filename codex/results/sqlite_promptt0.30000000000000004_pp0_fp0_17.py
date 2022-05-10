import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# SQLite database filename
db_filename = "test.db"

# Connect to the database
conn = sqlite3.connect(db_filename)

# Create a table
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE test
(
    id INTEGER PRIMARY KEY,
    description VARCHAR(100)
)
""")

# Insert some data
cursor.execute("""
INSERT INTO test (description) VALUES ('Hello, world')
""")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
# Test sqlite3.connect()

# SQLite database filename
db_filename = "test.db"

# Connect to the database
conn = sqlite3.connect(db_filename)

# Create a table
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE test
(
    id INTEGER
