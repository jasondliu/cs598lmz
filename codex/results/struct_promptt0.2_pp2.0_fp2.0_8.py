import _struct
# Test _struct.Struct.pack_into()

import array
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_pack_into(self):
        # Issue #11459: _struct.Struct.pack_into() should accept buffer objects
        # as well as mutable byte arrays.
        s = _struct.Struct('i')
        a = array.array('b', b'\0' * s.size)
        buf = memoryview(a)
        s.pack_into(buf, 0, 42)
        self.assertEqual(a.tolist(), [42, 0, 0, 0])
        self.assertEqual(s.pack_into(buf, 0, sys.maxsize), None)
        self.assertEqual(a.tolist(), [127, -1, -1, -1])

        # Issue #11459: _struct.Struct.pack_into() should accept read-only
        # buffer objects.
        a = array.array('b', b'\0' * s.size)
       
