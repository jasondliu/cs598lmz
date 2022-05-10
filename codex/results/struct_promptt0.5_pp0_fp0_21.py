import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(s.pack(1)), (1,))
        self.assertEqual(s.unpack(s.pack(0)), (0,))
        self.assertEqual(s.unpack(s.pack(-1)), (-1,))
        self.assertEqual(s.unpack(s.pack(sys.maxsize)), (sys.maxsize,))
        self.assertEqual(s.unpack(s.pack(sys.maxsize+1)), (sys.maxsize+1,))
        self.assertEqual(s.unpack(s.pack(-sys.maxsize-1)), (-sys.maxsize-1,))
        self.assertEqual(s.unpack(s.pack(-sys.maxsize-2)), (-sys.maxsize-2,))

        s = _struct.Struct('q
