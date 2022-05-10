import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/t1.db')
DBNAME = './gpustat.db'


class GPUStat:
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.handle = self.libc.dlopen(ctypes.c_char_p('/usr/local/lib/libgpustat.so'), self.libc.RTLD_NOW)
        # print self.handle
