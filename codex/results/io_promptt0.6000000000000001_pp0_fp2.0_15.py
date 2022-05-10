import io
# Test io.RawIOBase
# Test io.RawIOBase.readinto

import _io

# Issue #8496: check that the docstring is not the one of object.__init__
assert io.RawIOBase.__init__.__doc__

# Test RawIOBase
class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.readinto_calls = 0
        self.read_calls = 0
        self.writable = True

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        pass

    def tell(self):
        return 0

    def readinto(self, b):
        self.readinto_calls += 1
        return len(b)

    def read(self, n=-1):
        self.read_calls += 1
        return b"x"*n

rawio = TestRawIO()
buf = bytearray(100)
n = rawio.readinto(buf)

