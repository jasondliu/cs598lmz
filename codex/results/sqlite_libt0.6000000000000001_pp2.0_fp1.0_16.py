import ctypes
import ctypes.util
import threading
import sqlite3

from wfdb_utils import *

wfdb = ctypes.CDLL(ctypes.util.find_library('wfdb'))
wfdb.isigopen.restype = ctypes.c_int

class PhysioRecord:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
        self.db = sqlite3.connect(name + '.db')
        self.db.row_factory = sqlite3.Row
        self.db.execute('CREATE TABLE IF NOT EXISTS physio (sample_num INTEGER PRIMARY KEY, ' +
                        'sample_time REAL, ' +
                        'sample_value REAL)')
        self.db.commit()
        self.samples = []
        self.sample_times = []
        self.sample_values = []
        self.sample_index = 0
        self.start_time = 0
        self.sample_freq = 0
        self.sample_count = 0
        self.isig = None
       
