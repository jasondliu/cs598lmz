import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref
import os
import errno

from test import support


class MockRawIO(io.RawIOBase):

    def __init__(self, read_stack=()):
        self._read_stack = iter(read_stack)

    def readable(self):
        return True

    def readinto(self, buf):
        try:
            data = next(self._read_stack)
        except StopIteration:
            return None
        if isinstance(data, OSError):
            raise data
        buf[:len(data)] = data
        return len(data)


class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        b = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, b.read)
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray())

    def test_readinto(self):
        b = MockRawIO(b"abc")

