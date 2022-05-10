import _struct
# Test _struct.Struct(format).unpack(buffer)
#
# XXX This test is incomplete.  More data types need to be added.
import _struct
import unittest


class StructTest(unittest.TestCase):
    def test_unsigned_char(self):
        s = _struct.Struct('B')
        self.assertEqual(s.unpack(b'\x00'), (0,))
        self.assertEqual(s.unpack(b'\x01'), (1,))
        self.assertEqual(s.unpack(b'\x7f'), (127,))
        self.assertEqual(s.unpack(b'\x80'), (128,))
        self.assertEqual(s.unpack(b'\xff'), (255,))

    def test_char(self):
        s = _struct.Struct('b')
        self.assertEqual(s.unpack(b'\x00'), (0,))
        self.assertEqual(s.unpack(b'\x01'), (1,))
