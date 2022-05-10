import _struct
# Test _struct.Struct.
import struct as stdlib_struct

import unittest
from test import test_support


class StructTestCase(unittest.TestCase):

    def test_basic(self):
        s = _struct.Struct("hi 12s i")
        self.assertEqual(s.size, 14)
        self.assertEqual(s.pack(1, "junk", 2),
                         stdlib_struct.pack("hi 12s i", 1, "junk", 2))
        self.assertEqual(s.unpack(_struct.pack("hi 12s i", 1, "junk", 2)),
                         (1, "junk", 2))
        self.assertEqual(s.unpack_from(buffer("xxx" +
                                              _struct.pack("hi 12s i",
                                                           1, "junk", 2))),
                         (1, "junk", 2))
        self.assertEqual(s.calcsize(), 14)

    def test_bool(self):
        s = _struct.Struct("?")
        self.assert
