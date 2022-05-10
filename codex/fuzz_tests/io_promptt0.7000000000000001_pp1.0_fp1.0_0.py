import io
# Test io.RawIOBase for readinto
#
# Reuse the test for io.BytesIO

from test import test_support
import unittest

class TestBytesIO(io.BytesIO):
    def readinto(self, b):
        # Call the super to raise the exception if the buffer is too small
        io.BytesIO.readinto(self, b)
        return self.readinto1(b)

    def readinto1(self, b):
        data = self.getvalue()
        n = len(b)
        if n > len(data):
            n = len(data)
        b[:n] = data
        return n

class TestRawIO(TestBytesIO, io.RawIOBase):
    pass

class TestBufferedIO(TestRawIO, io.BufferedIOBase):
    pass

class TestReadinto(unittest.TestCase):
    def test_readinto(self):
        b = bytearray(5)
        f = TestBufferedIO(b"12345")
        n = f.readinto(b)
        self
