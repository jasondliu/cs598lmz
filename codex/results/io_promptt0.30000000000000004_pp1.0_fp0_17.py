import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11395: check that io.RawIOBase is an ABC
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, None)

    def test_read(self):
        # Issue #11395: check that io.RawIOBase.read() is a virtual method
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        rawio = MyRawIO()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.read, 0)

    def test_readinto(self):
        # Issue #11395: check that io.RawIOBase.readinto() is a virtual method
        class MyRawIO(io.RawIO
