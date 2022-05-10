import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() to see if we can run this program
try:
    sqlite3.connect(":memory:")
except:
    print("\nThis program requires Python 3.x and sqlite3\n")
    sys.exit(1)
import argparse
import traceback

#
# A class to hold the information associated with a single
# connection to a database.
#
class ConnInfo:
    def __init__(self, dbname, conn, filename):
        self.dbname = dbname
        self.conn = conn
        self.filename = filename
        self.dirty = False
        self.lock = threading.Lock()

    def __del__(self):
        self.lock.acquire()
        self.conn.close()
        self.lock.release()

#
# A class to hold the information associated with a single
# database to be opened.
#
class DbInfo:
    def __init__(self, filename, dbname):
        self.filename = filename
        self.dbname = dbname
        self.conn = None

#
#
