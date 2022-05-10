import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"x" * n
    def write(self, b):
        return len(b)

class MyRawIO2(_io.RawIOBase):
    def read(self, n=-1):
        return b"x" * n
    def write(self, b):
        return len(b)
    def seekable(self):
        return False

class MyRawIO3(_io.RawIOBase):
    def read(self, n=-1):
        return b"x" * n
    def write(self, b):
        return len(b)
    def readable(self):
        return False

class MyRawIO4(_io.RawIOBase):
    def read(self, n=-1):
        return b"x" * n
    def write(self, b):
        return len(b)
    def writable(self):
        return False

class MyRawIO5(_io.RawIOBase):
   
