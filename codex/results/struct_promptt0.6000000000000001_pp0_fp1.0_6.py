import _struct
# Test _struct.Struct
import struct
from test import test_support
from test.test_support import run_unittest

class StructTest(unittest.TestCase):
    def test_format_size(self):
        for format, size in [('x', 1),
                             ('c', 1),
                             ('b', 1),
                             ('B', 1),
                             ('h', 2),
                             ('H', 2),
                             ('i', 4),
                             ('I', 4),
                             ('l', 4),
                             ('L', 4),
                             ('q', 8),
                             ('Q', 8),
                             ('f', 4),
                             ('d', 8)]:
            self.assertEqual(_struct.calcsize(format), size)

    def test_pack(self):
        for format, input, output in [('x', '', '\x00'),
                                      ('c', 'x', 'x'),
                                      ('b', 1, '\x01'),
                                      ('B', 1, '\x01'),
                                      ('h',
