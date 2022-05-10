import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self):
        return self.file.read()
    def write(self, data):
        self.file.write(data)
    def close(self):
        self.file.close()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

import os
import sys

class Console(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def read(self, size=None):
        if size is None:
            return os.read(self.fd, 4096)
        else:
            return os.read(self.fd, size)
    def write(self, b):
        return os.write(self.fd, b
