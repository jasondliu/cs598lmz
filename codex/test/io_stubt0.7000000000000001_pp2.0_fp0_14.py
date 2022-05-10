import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

'''
>>> import test_io
>>> test_io.view
bytearray(b'\x00')
'''

# ____________________________________________________________
#
# ctypes-based test

from ctypes import *

class File(object):
    def __init__(self):
        self.file = c_void_p.in_dll(cdll, 'stdin')
        self.buffer = None
    def readinto(self, buf):
        global view
        self.buffer = buf
        view = buf
        return len(buf)
    def readable(self):
        return True

