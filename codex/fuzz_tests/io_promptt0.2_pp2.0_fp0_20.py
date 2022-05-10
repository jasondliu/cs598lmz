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
    def seek(self, pos, whence=0):
        pass
    def tell(self):
        return 42
    def truncate(self, pos=None):
        pass
    def fileno(self):
        return 42

class MyRawIO3(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        pass
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        pass
    def tell(self):
        return 42
    def truncate(self, pos=None
