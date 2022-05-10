import _struct
# Test _struct.Struct class.
import unittest
from test.support import bigmemtest, run_unittest
import io
from decimal import Decimal
class StructTestCase(unittest.TestCase):
    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(3), b'\x03\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x03\x00\x00\x00'), (3,))
        self.assertEqual(s.pack_into(bytearray(), 0, 3), 4)
        self.assertEqual(len(bytearray()), 0)
        self.assertEqual(s.unpack_from(b'\x03\x00\x00\x00'), (3,))
