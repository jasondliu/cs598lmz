import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

# TODO:
# - test with multiple threads
# - test with multiple processes
# - test with multiple processes and threads
# - test with multiple processes and threads and multiple databases
# - test with multiple processes and threads and multiple databases and multiple connections
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and multiple statements
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and multiple statements and multiple results
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and multiple statements and multiple results and multiple rows
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and multiple statements and multiple results and multiple rows and multiple columns
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and multiple statements and multiple results and multiple rows and multiple columns and multiple values
# - test with multiple processes and threads and multiple databases and multiple connections and multiple cursors and
