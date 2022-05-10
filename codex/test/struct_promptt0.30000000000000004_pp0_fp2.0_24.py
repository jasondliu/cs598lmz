import _struct
# Test _struct.Struct.__repr__

import test.support
import unittest

class StructTest(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(_struct.Struct('i')),
                         "<class '_struct.Struct'>('i')")
        self.assertEqual(repr(_struct.Struct('i').format), 'i')
        self.assertEqual(repr(_struct.Struct('i').size), _struct.calcsize('i'))

    def test_unpack(self):
        self.assertEqual(_struct.Struct('i').unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(_struct.Struct('i').unpack(b'\xff\xff\xff\xff'), (-1,))
        self.assertEqual(_struct.Struct('i').unpack(b'\x01\x00\x00\x00'), (1,))
