import _struct
# Test _struct.Struct to be sure it works
# i.e. does it produce all the expected results as shown in the doc.

import _struct
import unittest
from test.support import run_unittest

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('=hhl')

        self.assertEqual(s.format, '=hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), b'\x00\x01\x00\x02\x00\x00\x00\x03')
        self.assertEqual(s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(s.unpack_from(_struct.EMPTYBUF, 0), (0, 0, 0))
        self.assertEqual(s.unpack_
