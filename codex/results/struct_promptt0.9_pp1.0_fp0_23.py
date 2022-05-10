import _struct
# Test _struct.Struct with nested structs
#
import _struct
import unittest

# The struct module lacks support for nesting structs, so tests are below:

class SimpleNestingTests(unittest.TestCase):
    def test_unpack_single_level_nest(self):
        header_format = 'i5si5s'
        header_size = 20
        nested_format = 'i5s'
        s = _struct.Struct(header_format)
        b = b'1234hello5678world'
        self.assertEqual(s.size, header_size)
        self.assertEqual(s.unpack(b), (1234, b'hello', 5678, b'world'))

    @support.bigmemtest(size=support.big_endian + support.big_endian)
    def test_unpack_two_level_nest(self, sz):
        class TwoLevels(object):
            def __init__(self, x1, x2, x3):
                self.value = x1
                self.next =
