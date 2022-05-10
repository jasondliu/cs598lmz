import _struct
# Test _struct.Struct.

import struct
import unittest
from test import test_support


class StructTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(_struct.Struct('i').size, struct.calcsize('i'))
        self.assertEqual(_struct.Struct('i').pack(42), struct.pack('i', 42))
        self.assertEqual(_struct.Struct('i').unpack(struct.pack('i', 42)),
                         (42,))
        self.assertEqual(_struct.Struct('i').unpack_from(struct.pack('i', 42)),
                         (42,))
        self.assertEqual(_struct.Struct('i').pack_into(bytearray(4), 0, 42), None)
        self.assertEqual(_struct.Struct('i').unpack_from(bytearray(struct.pack('i', 42))),
                         (42,))

    def test_error_cases(self):
        s = _struct.Struct('i')
