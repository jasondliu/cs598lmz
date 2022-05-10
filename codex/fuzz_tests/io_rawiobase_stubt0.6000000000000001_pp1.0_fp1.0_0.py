import io
class File(io.RawIOBase):
    def read(self, n=-1):
        pass
    def readinto(self, b):
        pass
    def write(self, b):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def tell(self):
        pass
    def truncate(self, size=None):
        pass
    def flush(self):
        pass
    def close(self):
        pass
    def fileno(self):
        pass

import collections.abc
class TextIOBase(io.RawIOBase):
    def read(self, n=-1):
        pass
    def readline(self, limit=-1):
        pass
    def readlines(self, hint=-1):
        pass
    def write(self, s):
        pass
    def writelines(self, lines):
        pass

class IncrementalNewlineDecoder(collections.abc.Iterator):
    def __init__(self, errors='strict'):
        pass
    def decode(self, b, final=False):
        pass
   
