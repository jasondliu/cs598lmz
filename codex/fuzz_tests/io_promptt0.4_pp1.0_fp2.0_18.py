import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_readinto2(self):
        # Issue #12561: readinto() should accept any writable buffer
        class MockRawIO(io.RawIOBase):
            def readinto(self, b):
                return super(MockRawIO, self).readinto(memoryview(b))

        b = bytearray(10)
        self.assertEqual(MockRawIO().readinto(b), 0)
        self.assertEqual(MockRawIO().readinto(memoryview(b)), 0)
        self.assertEqual(MockRawIO().readinto(array.array('b', b
