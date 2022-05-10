import io
# Test io.RawIOBase

import io
import unittest
import weakref

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test RawIOBase
        io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().seek, 0)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().tell)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().truncate)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().flush)
        self.assertRaises(io
