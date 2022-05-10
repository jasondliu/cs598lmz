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
        if not self.handle:
            print 'Failed to load the shared object'
        else:
            print 'Succeed to load the shared object'
            self.init = self.libc.get_gpu_stat
            self.init.restype = ctypes.POINTER(ctypes.c_char_p * 2 * 6 + ctypes.c_int)
            # print self.init()

            self.profiling = self.libc.profiling_kernel
            self.profiling.restype = ctypes.c_int
            self.profiling.argtypes = [ct
