import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Make sure we have ctypes
try:
    ctypes.CDLL("libc.so.6")
except:
    print("This test requires ctypes")
    raise SystemExit

# Make sure we have the sqlite3 library
lib = ctypes.util.find_library("sqlite3")
if not lib:
    print("This test requires libsqlite3")
    raise SystemExit

# Make a small SQL script
with open("test.sql", "w") as f:
    f.write("""
    CREATE TABLE tbl1(one VARCHAR(10), two SMALLINT);
    INSERT INTO tbl1 VALUES('hello!', 10);
    INSERT INTO tbl1 VALUES('goodbye', 20);
    """)

# Create a connection
con = sqlite3.connect(":memory:")

# Run the script
with open("test.sql") as f:
    con.executescript(f.read())

# Run a select to verify the data
with con:
    cur = con.c
