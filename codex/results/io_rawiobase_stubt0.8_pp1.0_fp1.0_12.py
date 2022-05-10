import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return False
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def __enter__(self):
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

from collections import defaultdict
from copy import copy
#from .gold.histogram
