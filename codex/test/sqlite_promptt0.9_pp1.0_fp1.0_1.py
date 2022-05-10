import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("data.sqlite")
# sqlite3.complete_statement("select * from testino")
import sys
import traceback
import collections

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


debug = False
startup = False
class Myysqldb:
    def __init__(self, port):
        self.port = port
        self.server = None
        self.request = sqlite3.connect("data.sqlite")   # The database that stores the data of this database
        self.q = {}
        self.q_log = []
        self.q_n = 0
        self.threads = set()
        self.running = True
        self.sqllock = Lock()
        self.shm = WorkerShm()
        self.workers = []
        self.workercounter = 0
        self.data = {}
        self.isdirty = set()
        self.data_lock = RLock()
    def init(self):
        self.create_tables()
