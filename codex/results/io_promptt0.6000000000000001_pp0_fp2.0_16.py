import io
# Test io.RawIOBase

import _io

# Test classes

class MyIO(_io.RawIOBase):

    def __init__(self, value):
        self.value = value
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.value): return None
        data = self.value[self.pos:self.pos+n]
        n = len(data)
        b[:n] = data
        self.pos += n
        return n

    def write(self, b):
        self.value += b
        self.pos += len(b)
        return len(b)

class TestRawIOBase:

    def test_attributes(self):
        io.RawIOBase()
        io.BufferedIOBase()
        io.TextIOBase()

    def test_io_methods(self):
        # This only tests the parts of the RawIOBase interface
        # that are implemented by BufferedReader
        m = MyIO(b"ab")
        assert m.readable
