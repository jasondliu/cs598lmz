import _struct
# Test _struct.Struct

import struct
import unittest

# Test _struct.Struct
class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(struct.Struct('i').size, _struct.Struct('i').size)
        self.assertEqual(struct.Struct('i').pack(42),
                         _struct.Struct('i').pack(42))
        self.assertEqual(struct.Struct('i').unpack(_struct.Struct('i').pack(42)),
                         (42,))
        self.assertEqual(struct.Struct('i').unpack_from(_struct.Struct('i').pack(42), 0),
                         (42,))
        self.assertEqual(struct.Struct('i').unpack_from(_struct.Struct('i').pack(42) + b'\x00\x00', 0),
                         (42,))
