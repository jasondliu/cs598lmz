import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() behavior
print()
print('*** sqlite3.connect() with no args ***')
conn_noargs = sqlite3.connect()

print('*** sqlite3.connect() with connection string and no kwargs ***')
conn_str = sqlite3.connect('example.db')

print('*** sqlite3.connect() with connection string and kwargs ***')
conn_str_kwargs = sqlite3.connect('example.db', timeout = 5, isolation_level = None)

print('*** sqlite3.connect() with database and no kwargs ***')
conn_db = sqlite3.connect(':memory:')

print('*** sqlite3.connect() with database and read-only kwarg ***')
conn_db_ro = sqlite3.connect(':memory:', readonly = True)
conn_str_kwargs.close()
conn_str.close()
conn_db_ro.close()
conn_db.close()
conn_noargs.close()
# Test sqlite3.Row
print()
print('*** sqlite3.
