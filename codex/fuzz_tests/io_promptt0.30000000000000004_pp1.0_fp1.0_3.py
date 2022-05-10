import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def seek(self, n, whence=0):
        return 0
    def tell(self):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def close(self):
        pass

class MyRawIO2(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def seek(self, n, whence=0):
        return 0
    def tell(self):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def close(self):
        pass

class MyRawIO3
