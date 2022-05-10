import io
# Test io.RawIOBase
import io
import sys

class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n

class RawO(io.RawIOBase):
    def write(self, b):
        self.b = b

class RawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n
    def write(self, b):
        self.b = b

class TestRawIOBase(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, RawI().read)

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, RawI().readall)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, RawI().readinto, b'')

    def test_readinto_
