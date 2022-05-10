import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections
# The first connection will be used as a reference for the others
# - the first connection will be used for all locking
# - the first connection will be used for all global queries

# A new connection will be made for each thread that is started
# - each thread has a unique connection
# - each connection will be use for local queries
# - each connection will have its own cursor

# The reference connection will be used to create the schema
# - a new table will be created for each thread
# - table names will be in the format of "<thread name>-<table number>"

# The reference connection will be used to create triggers
# - triggers will be created for each table
# - triggers will be of the form "init_<thread name>_<table number>"
# - triggers will be of the form "upd_<thread name>_<table number>"

# The reference connection will be used to create stored procedures
# - procedures will be created for each thread
# - procedures will be of the form "proc_<thread name>_<table number>"

# The reference connection will be used to create stored functions
# -
