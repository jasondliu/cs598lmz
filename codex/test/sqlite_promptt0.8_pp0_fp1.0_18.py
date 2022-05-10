import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# then sqlite3.cursor()
# then sqlite3.execute()
# then sqlite3.close()

# Test sqlite3.connect()
# connect() should fail with bad URL
# connect() should fail with bad File
# connect() should fail with bad OpenFlags
# connect() should fail with bad VFS
# connect() should fail with bad Authorization
# connect() should succeed with good URL
# connect() should succeed with good File
# connect() should succeed with good OpenFlags
# connect() should succeed with good VFS
# connect() should succeed with good Authorization
# connect() should succeed with good UserAuthorization
# connect() should succeed with None Authorization
# connect() should succeed with empty Authorization

# Test sqlite3.cursor()
# cursor() should fail with bad connection
# cursor() should succeed with good connection

# Test sqlite3.execute()
# execute() should fail with bad cursor
# execute() should fail with bad sql
# execute() should fail with bad parameters
# execute() should fail with bad multiple statements
# execute() should fail with wrong number of parameters
# execute() should fail
