import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# https://stackoverflow.com/questions/30293825/python-multiprocessing-and-sqlite3-database-locking
# https://stackoverflow.com/questions/11657879/python-sqlite3-and-multithreading
# https://stackoverflow.com/questions/1726402/in-python-how-do-i-use-a-shared-sqlite-database-connection-in-a-multiprocess-pro
# https://stackoverflow.com/questions/10508898/how-to-share-a-sqlite-database-connection-between-processes
# https://stackoverflow.com/questions/1726402/in-python-how-do-i-use-a-shared-sqlite-database-connection-in-a-multiprocess-pro
# https://stackoverflow.com/questions/10508898/how-to-share-a-sqlite-database-connection-between-processes
# https://stackover
