import _struct
# Test _struct.Struct.format
#
# This tests that the format string is parsed correctly, and that the
# resulting Struct object has the right size.

import _struct
from test.test_support import run_unittest
from test import test_support

class StructTest(unittest.TestCase):

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 42)
        self.assertRaises(TypeError, _struct.Struct, 'ii', 42)

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')

        s = _struct.Struct('ii')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.format, 'ii')

        s = _struct.Struct('hhh')
        self.assertEqual(s.size, 6)
        self.assertEqual(s.format, 'hhh')

        s = _
