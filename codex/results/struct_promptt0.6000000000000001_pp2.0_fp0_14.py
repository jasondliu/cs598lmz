import _struct
# Test _struct.Struct.
# Also test that Struct can be pickled, copied and deepcopied.
# Also test that _struct.error is an exception class.

import pickle
import copy
import copyreg
import unittest

from test import support
from test.support import bigmemtest
import struct

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Test the saner parts of the struct module
        s = _struct.Struct("i")
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b"\x39\x30\x00\x00")
        self.assertEqual(s.pack(-12345), b"\xc7\xcf\xff\xff")
        self.assertEqual(s.unpack(b"\x39\x30\x00\x00"), (12345,))
        self.assertEqual(s.unpack(b"\xc7\xcf\xff\xff"), (-12345,))
        if support.HAVE
