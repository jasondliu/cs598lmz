import _struct
# Test _struct.Struct with native String types
import test
import test.support as support
import unittest
import pickle


class ByteTests(unittest.TestCase):
    #
    # Test _struct.Struct with native String
    #

    def setUp(self):
        self.s = _struct.Struct("@c")

    def test_zeroes(self):
        #
        # _struct.Struct.pack should return a bytearray of the given byte length
        #

        # 'c' argument forced to int, then to bytes
        self.assertEqual(self.s.pack(0), b'\x00')
        self.assertEqual(self.s.pack(b'\x00'), b'\x00')
        self.assertRaises(TypeError, self.s.pack)

    def test_byte_length(self):
        #
        # _struct.Struct should have a size attribute that
        # matches the length of the packed struct (as a byte)
        #

        self.assertEqual(self.s.size, 1)

