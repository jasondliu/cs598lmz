import _struct
# Test _struct.Struct

from struct import Struct
from _struct import pack
from collections import namedtuple
try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence

from test import support
import unittest


class StructTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(Struct('i').size, 4)
        self.assertEqual(Struct('i').pack(42), pack('i', 42))
        self.assertEqual(Struct('i').unpack(pack('i', 42))[0], 42)
        self.assertRaises(struct.error, Struct, 'Z')

    def test_iterator_unpack(self):
        s = Struct('hhl')
        data = s.pack(1, 2, 3)
        iterable = s.iter_unpack(data)
        self.assertEqual(type(iterable), type(iter(data)))
        self.assertEqual(list(s.iter_unpack(data)), [(1, 2, 3)])
        # Test repeated
