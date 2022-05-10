import io
# Test io.RawIOBase.readinto()

import _io
import unittest

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test that readinto() works on a RawIOBase
        class TestRawIO(_io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b"foo"
                return 3
        b = bytearray(5)
        self.assertEqual(TestRawIO().readinto(b), 3)
        self.assertEqual(b, b"foobl")
        self.assertEqual(TestRawIO().readinto(memoryview(b)), 3)
        self.assertEqual(b, b"foobl")
        self.assertRaises(TypeError, TestRawIO().readinto, b"")
        self.assertRaises(TypeError, TestRawIO().readinto, bytearray())
        self.assertRaises(TypeError, TestRawIO().readinto, memoryview(b"abc"))

