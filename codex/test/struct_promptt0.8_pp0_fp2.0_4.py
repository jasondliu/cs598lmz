import _struct
# Test _struct.Struct
import unittest
import struct, sys
from test import test_support

class StrStructTestCase(unittest.TestCase):

    def test_basics(self):
        for code in 'xbhilfd':
            s = struct.Struct(code)
            self.assertEqual(s.size, struct.calcsize(code))
            self.assertEqual(s.format, code)
            self.assertRaises(TypeError, s.pack, 1, 2)
            if code in 'xbh':
                self.assertRaises(struct.error, s.pack, 256)
            elif code in 'il':
                self.assertRaises(struct.error, s.pack, 2147483648)
            elif code == 'f':
                self.assertRaises(TypeError, s.pack)
                self.assertRaises(struct.error, s.pack, 1, 2)
                self.assertRaises(TypeError, s.pack, 1, 2.0, 3)
                # the following test does not make sense for other structs

