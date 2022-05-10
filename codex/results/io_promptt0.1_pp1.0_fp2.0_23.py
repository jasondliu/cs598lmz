import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "RawIOBase is missing the 'mode' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "RawIOBase is missing the 'name' attribute")

    def test_abc(self):
        self.assertTrue(io.RawIOBase.readinto(bytearray(1)) is None)
        self.assertTrue(io.RawIOBase.readinto1(bytearray(1)) is None)
        self.assertTrue(io.RawIOBase.readall() is None)
        self.assertTrue(io.RawIOBase.read() is None)
        self.assertTrue(io.RawIOBase.read1() is None)
        self.assertTrue(io.RawIOBase.write(b"") is None)
        self.assertTrue
