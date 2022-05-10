import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# https://stackoverflow.com/questions/17087446/how-to-share-a-sqlite-database-connection-between-multiple-processes-in-python
# https://stackoverflow.com/questions/28284996/sqlite3-shared-cache-in-python
# https://stackoverflow.com/questions/17087446/how-to-share-a-sqlite-database-connection-between-multiple-processes-in-python
# https://stackoverflow.com/questions/28284996/sqlite3-shared-cache-in-python
# https://stackoverflow.com/questions/17087446/how-to-share-a-sqlite-database-connection-between-multiple-processes-in-python
# https://stackoverflow.com/questions/28284996/sqlite3-shared-cache-in-python
# https://stackoverflow.com/questions/17087446/how-to-share
