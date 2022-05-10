import io
# Test io.RawIOBase
import io
import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        return len(b)

class MyRawIO2(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"xyz"
        return 3
    def write(self, b):
        return len(b)

class MyRawIO3(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"xyz"
        return 3
    def write(self, b):
        return len(b)
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        return 0
    def tell(self):
        return 0

class MyRawIO4(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"xyz"
        return 3
    def write(
