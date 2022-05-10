import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Start to looping thread write/read over database.

# Path database
db_path = "/var/lib/pxc-join/pxc-join.db"

# Create connection database
conn = sqlite3.connect(db_path, check_same_thread = False)

def check_database(n):
  # Exec query READ
  f = conn.execute("SELECT 1")

  # Fetch result
  r = f.fetchall()
  print("#%s\n" % n)
  print("READ result: ")
  print("%s" % r)

# Create Thread
# If conn.execute("SELECT 1") be executed multiple times without other operations, sqlite3.OperationalError: database is locked would get.
def concurrent_query_without_lock(n):
  for i in range(5):
    check_database(n)


# If using conn.commit(), sqlite3.OperationalError: database is locked would not get.
def concurrent_query_with_lock(n):
  for i in range
