import io
# Test io.RawIOBase
class MyRawIOBase(io.RawIOBase):
    def readinto(self, b):
        return 0
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

MyRawIOBase()
# Test io.BufferedIOBase
class MyBufferedIOBase(io.BufferedIOBase):
    def readinto(self, b):
        return 0
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

MyBufferedIOBase()
# Test io.TextIOBase
class MyTextIOBase(io.TextIOBase):
    def readinto(self, b):
        return 0
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

MyTextIOBase()
# Test io.RawIOBase.readinto()
