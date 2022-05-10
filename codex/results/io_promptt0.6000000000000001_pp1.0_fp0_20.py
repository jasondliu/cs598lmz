import io
# Test io.RawIOBase.readinto()

import sys
import unittest
from test import support

class BytesIO(io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self._buf = bytearray(initial_bytes)
        self._pos = 0

    def readinto(self, b):
        end = min(len(self._buf), self._pos + len(b))
        b[:end - self._pos] = self._buf[self._pos:end]
        self._pos = end
        return end - self._pos

    def write(self, b):
        self._buf.extend(b)
        return len(b)

    def pos(self):
        return self._pos


class TestReadinto(unittest.TestCase):

    def test_readinto(self):
        # Read bytes into existing buffer
        f = BytesIO(b'hello world')
        b = bytearray(5)
        n = f.readinto(b)
        self.assertEqual(n, 5)
