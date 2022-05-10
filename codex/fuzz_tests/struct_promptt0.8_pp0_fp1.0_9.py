import _struct
# Test _struct.Struct.
from test import support


class StructTest(unittest.TestCase):
    def test_struct_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        # Check that that we can unpack a string
        self.assertEqual(s.unpack('\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack('\x00\x00\x00\x00'), (0,))
        self.assertEqual(s.unpack('\xff\xff\xff\xff'), (-1,))
        self.assertRaises(TypeError, s.unpack, b'1234')
        # Check that we check for the exact value
        self.assertRaises(struct.error, s.unpack, '\x01\x00\x00')
        self.assertRaises(struct.error, s.unpack, '\x01\x00\x00\x00\x00')


@unittest.skip
