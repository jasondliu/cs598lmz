import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_abc_override(self):
        # test abstractmethod overrides
        class MyRawIO(_io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertRaises(io.UnsupportedOperation, MyRawIO().read, 0)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().write, b'')

    def test_detach(self):
        # Test RawIOBase.detach()
        class MyRawIO(_io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertRaises(io.UnsupportedOperation, MyRawIO().detach)

    def test_read(self):
        # Test RawIOBase.read()
        class MyRawIO(_
