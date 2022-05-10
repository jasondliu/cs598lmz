import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.create_function("sha1",1,sha1)
# Test sqlite3.connection.create_aggregate("sha1",1,sha1)
# Test sqlite3.connection.create_aggregate("sha1",1,sha1,sha1_final)

# Test sqlite3.connection.create_function("split",2,split)
# Test sqlite3.connection.create_function("split",2,split,True)
# Test sqlite3.connection.create_function("split",2,split,False)

# Test sqlite3.connection.create_function("split",2,split,True,True)
# Test sqlite3.connection.create_function("split",2,split,True,False)
# Test sqlite3.connection.create_function("split",2,split,False,True)
# Test sqlite3.connection.create_function("split",2,split,False,False)

# Test sqlite3.connection.create_function("split",2,split,False,False,True)
# Test sqlite3.connection.create_function
