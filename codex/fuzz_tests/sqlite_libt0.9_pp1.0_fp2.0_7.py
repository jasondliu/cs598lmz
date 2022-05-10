import ctypes
import ctypes.util
import threading
import sqlite3
import os
_pg = None
_pgdir = None

class pg:
    def __init__(self):
        global _pgdir
        if _pgdir is None:
            try:
                _pgdir = ctypes.util.find_library('pq')
            except:
                _pgdir = None
        if _pgdir:
            dlltype = ctypes.CDLL
        else: #platform.system() == 'Windows':
            try:
                lib = os.environ['POSTGRESDLL']
            except KeyError:
                raise ValueError('POSTGRESDLL environment variable not set. Cannot load library.')
            dlltype = ctypes.windll.LoadLibrary
        self.dll = dlltype(_pgdir)
    def writeline(self,s,pyout=None):
        if pyout is None:
            pyout = sys.stdout
        pyout.write(str(s)+'\n')

    def readline(self,pyin=None):
        if pyin is None:
            pyin = sys.
