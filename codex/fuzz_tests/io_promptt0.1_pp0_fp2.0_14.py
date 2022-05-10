import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        pass

class MyRawIO2(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        pass
    def seekable(self):
        return True
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def truncate(self, n=None):
        pass

class MyRawIO3(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        pass
    def seekable(self):
        return True
    def seek(self, n, whence=0):
        pass
    def tell(self):
        return 0
    def truncate(self, n=None):
        pass
    def readable(self):

