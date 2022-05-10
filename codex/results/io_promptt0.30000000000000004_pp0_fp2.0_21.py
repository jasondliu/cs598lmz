import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_args(self):
        # Test RawIOBase constructor
        self.assertRaises(TypeError, io.RawIOBase)
        self.assertRaises(TypeError, io.RawIOBase, "foo")

    def test_attrs(self):
        # Test RawIOBase attributes
        b = io.RawIOBase()
        self.assertEqual(b.mode, "")
        self.assertEqual(b.name, None)
        self.assertEqual(b.closed, False)
        b.close()
        self.assertEqual(b.closed, True)

    def test_read(self):
        # Test RawIOBase.read()
        b = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, b.read)
        self.assertRaises(io.UnsupportedOperation, b.read, 10)

    def test_readall(self):
