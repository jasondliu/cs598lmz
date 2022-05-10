import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        pass
    def write(self, s):
        pass
    def flush(self):
        pass
    def seekable(self):
        return True
    def writable(self):
        return True
    def fileno(self):
        return 1
    def isatty(self):
        return False

def open(name, mode, buffering=0):
    return File(name, mode)

def mod_import(name):
    return __builtin__.__import__('lol')
import __builtin__
__builtin__.open = open
__builtin__.__import__ = mod_import
__builtin__.flush = lambda: None

class MySerial(serial.Serial):
    def __init__(self, port, baudrate, timeout, writeTimeout):
        pass
    def flush(self):
        pass
    def write(self, s):
        pass
    def writeTimeout(self, s, timeout):
        pass
    def setRTS(self, level=1):

