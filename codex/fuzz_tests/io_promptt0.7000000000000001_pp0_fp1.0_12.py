import io
# Test io.RawIOBase compatibility

import unittest
from test import support

class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.readinto_calls = 0
        self.write_calls = 0
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        self.readinto_calls += 1
        return 42
    def write(self, b):
        self.write_calls += 1
        return len(b)

class RawIOTests(unittest.TestCase):

    def test_attributes(self):
        rawio = MyRawIO()
        self.assertEqual(rawio.mode, 'wb+')
        self.assertEqual(rawio.name, None)

    def test_readinto(self):
        rawio = MyRawIO()
        b = bytearray(100)
        n = rawio.readinto(b)
        self.assertE
