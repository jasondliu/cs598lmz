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
        self.assertTrue(io.RawIOBase.readinto(b"") is NotImplemented)
        self.assertTrue(io.RawIOBase.readall() is NotImplemented)
        self.assertTrue(io.RawIOBase.read() is NotImplemented)
        self.assertTrue(io.RawIOBase.write(b"") is NotImplemented)
        self.assertTrue(io.RawIOBase.seek(0) is NotImplemented)
        self.assertTrue(io.RawIOBase.tell() is NotImplemented)
