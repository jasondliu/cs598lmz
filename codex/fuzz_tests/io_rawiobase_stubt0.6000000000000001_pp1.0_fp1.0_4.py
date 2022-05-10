import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    
    def close(self):
        pass
    
    def read(self, size=-1):
        return b'0123456789'
    
    def write(self, b):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def flush(self):
        pass
    def fileno(self):
        return 1
    def readall(self):
        return b'0123456789'
    def readinto(self, b):
        b[:] = b'0123456789'
        return len(b)
    def write(self, b):
        pass
    def truncate(self, size=None):
        pass

import os
os.dup = os.dup2 = os.
