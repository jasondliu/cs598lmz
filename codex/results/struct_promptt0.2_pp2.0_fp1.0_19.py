import _struct
# Test _struct.Struct.pack_into()

import array
import sys
import unittest

from test import support

class StructTest(unittest.TestCase):
    def test_pack_into(self):
        # Test _struct.Struct.pack_into()
        s = _struct.Struct('i')
        a = array.array('b', b'\0' * s.size)
        s.pack_into(a, 0, 1)
        self.assertEqual(a.tostring(), b'\1\0\0\0')
        s.pack_into(a, 0, sys.maxsize)
        self.assertEqual(a.tostring(), b'\xff\xff\xff\7f')
        s.pack_into(a, 0, -1)
        self.assertEqual(a.tostring(), b'\xff\xff\xff\xff')
        s.pack_into(a, 0, -2)
        self.assertEqual(a.tostring(), b'\xfe\xff\xff\xff')
       
