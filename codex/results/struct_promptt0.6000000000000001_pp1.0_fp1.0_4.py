import _struct
# Test _struct.Struct

import struct
import unittest
from test import test_support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEquals(s.size, struct.calcsize('i'))
        self.assertEquals(s.format, 'i')

        values = (1, -2, 3.0, -4.0)
        for v in values:
            s = _struct.Struct('i')
            packed = s.pack(v)
            self.assertEquals(s.unpack(packed), (v,))

            s = _struct.Struct('I')
            packed = s.pack(v)
            self.assertEquals(s.unpack(packed), (v,))
            self.assertEquals(s.unpack_from(packed, 0), (v,))
            self.assertEquals(s.unpack_from(packed, 0), (v,))

            s = _struct.Struct('f')
            packed = s.pack
