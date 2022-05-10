import _struct
# Test _struct.Struct
from test import test_support
import unittest
from test.test_support import bigaddrspacetest

class StructTest(unittest.TestCase):

    def test_bool(self):
        # Issue #9180.
        # bool should be encoded as an integer, not a single character.
        s = _struct.Struct('?')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack(True), '\x01')
        self.assertEqual(s.pack(False), '\x00')
        self.assertEqual(s.unpack('\x01'), (True,))
        self.assertEqual(s.unpack('\x00'), (False,))

    def test_unpack_from(self):
        s = _struct.Struct('i')
        buf = buffer('abcdefgh')
        self.assertEqual(s.unpack_from(buf, 3), (1684234849,))
