import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        # RawIOBase defines read, readinto, write and seek
        self.assertTrue(hasattr(io.RawIOBase, 'read'))
        self.assertTrue(hasattr(io.RawIOBase, 'readinto'))
        self.assertTrue(hasattr(io.RawIOBase, 'write'))
        self.assertTrue(hasattr(io.RawIOBase, 'seek'))

    def test_abc(self):
        # RawIOBase is an abstract base class
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        # read()
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().read)

    def test_readinto(self):
        # readinto()
        self.assertRaises(io.UnsupportedOperation,
                          io.RawIOBase().
