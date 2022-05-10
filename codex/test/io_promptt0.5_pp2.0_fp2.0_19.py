import io
# Test io.RawIOBase.readinto
import io
import _io
import unittest
import sys


class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(b'abc')
        for i in range(len(b)):
            self.assertEqual(i, b.readinto(memoryview(b)[i:]))
        self.assertEqual(b'abc', b)
        self.assertRaises(TypeError, b.readinto, 'abc')
        self.assertRaises(TypeError, b.readinto, u'abc')
        self.assertRaises(TypeError, b.readinto, memoryview(b'abc'))
        self.assertRaises(TypeError, b.readinto, memoryview(u'abc'))
        self.assertRaises(TypeError, b.readinto, memoryview(b'abc'), 1)
        self.assertRaises(TypeError, b.readinto, memoryview(b), 1, 2, 3)
