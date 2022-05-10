import io
# Test io.RawIOBase.readinto
import _io
# Test _io.IOBase.readinto
import array
import struct
import sys
import unittest

class BytesIOTest(unittest.TestCase):

    def test_init(self):
        b = bytearray(b'abcdef')
        f = io.BytesIO(b)
        self.assertEqual(f.read(), b'abcdef')
        f.close()
        self.assertRaises(TypeError, io.BytesIO, 'abcdef')

        self.assertRaises(TypeError, io.BytesIO, bytearray(b'abcdef'), 42)

    def test_detach(self):
        b = bytearray(b'abcdef')
        f = io.BytesIO(b)
        self.assertRaises(AttributeError, getattr, f, 'buffer')
        self.assertEqual(f.detach(), b)
        self.assertRaises(ValueError, f.detach)
        f.close()

    def test_read(self):
       
