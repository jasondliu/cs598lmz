import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import os
import time

import numpy as np
import numpy.ctypeslib as npct

import lib

def sqlite_connect():
    return sqlite3.connect('/tmp/temperature.db')

class Temperature(object):
    def __init__(self, log=True):
        self.log = log
        self.lock = threading.Lock()
        self.libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

        self.array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS')
        self.lib = lib.get_lib()
        self.lib.temperature_init()

    def __del__(self):
        self.lib.temperature_close()
        if self.log:
            self.write_to_database()

    def temperature(self, channel):
        return self._temperature(channel)[0]

