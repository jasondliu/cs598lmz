import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() method
sqlite3.connect(':memory:')
sqlite3.connect('test.db')

# This is not a valid database connection
#sqlite3.connect('test/test.db')

# Test to see if sqlite3 has been compiled with threading
sqlite3.threadsafety

# Test to see if the sqlite3 connection object has been allocated
# (pysqlite is written in C and the C code uses malloc to allocate memory)
ctypes.CDLL(ctypes.util.find_library('c')).malloc(1)
# This is the working version of the code
# I'm not sure why the sqlite3.connect() method is not working
# when the "test" directory is included in the path


import sqlite3
import threading

# Test to see if sqlite3 has been compiled with threading
sqlite3.threadsafety

# Test to see if the sqlite3 connection object has been allocated
# (pysqlite is written in C and the C code uses malloc to allocate memory)
