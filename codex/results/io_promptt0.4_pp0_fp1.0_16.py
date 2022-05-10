import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)

class MyBufferedRawIO(_io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)

class MyBufferedRawIO2(_io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n

class MyBufferedRawIO3(_io.BufferedIOBase):
    def write(self, b):
        return len(b)

class MyBufferedRawIO4(_io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n
    def write(self, b):
        return len(b)
    def seek(self, n, whence=0):
        return 42

class MyBufferedRawIO5
