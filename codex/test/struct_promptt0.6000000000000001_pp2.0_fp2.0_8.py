import _struct
# Test _struct.Struct
#

import struct
from test.support import run_unittest, is_jython

class StructTest(unittest.TestCase):
    # Test _struct.Struct

    def test_basics(self):
        # Test the basics of Struct
        s = _struct.Struct('hi')
        self.assertEqual(s.size, 5)
        self.assertEqual(s.format, 'hi')
        self.assertEqual(s.pack(1, 2), b'\x00\x01\x00\x02')
        self.assertEqual(s.unpack(b'\x00\x01\x00\x02'), (1, 2))
        self.assertEqual(s.unpack_from(b'\x00\x01\x00\x02'), (1, 2))
        self.assertEqual(s.pack_into(b'\x00\x00\x00\x00\x00', 0, 1, 2), 5)
