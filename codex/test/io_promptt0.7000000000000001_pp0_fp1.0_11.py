import io
# Test io.RawIOBase
import io

class UnsupportedOperation(Exception):
    pass

class FakeRawIO(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0

try:
    FakeRawIO().read1(10)
except AttributeError:
    pass
else:
    raise Exception("should have raised AttributeError")

# Test io.BufferedReader
import io

class UnsupportedOperation(Exception):
    pass

class FakeRawIO(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0

