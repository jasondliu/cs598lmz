import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('/tmp/test.db')

# https://stackoverflow.com/questions/36947545/python-sqlite3-in-memory-database-is-not-thread-safe

# https://docs.python.org/2/library/sqlite3.html
# https://docs.python.org/3/library/sqlite3.html

# https://stackoverflow.com/questions/1026346/sqlite-and-concurrency
# https://stackoverflow.com/questions/36947545/python-sqlite3-in-memory-database-is-not-thread-safe
# https://stackoverflow.com/questions/7165749/open-file-in-binary-mode

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer
# https://docs.python
