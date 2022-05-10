import _struct
# Test _struct.Struct class

import test.test_support
import unittest
import sys

# Test _struct.Struct with a small struct format:
#     struct foo { short bar; };
class SmallStructTestCase(unittest.TestCase):
    def setUp(self):
        self.foo = _struct.Struct('h')
        self.foo_size = self.foo.size

    def test_format(self):
        self.assertEqual(self.foo.format, 'h')

    def test_size(self):
        self.assertTrue(self.foo_size >= 2)

    def test_pack(self):
        for v in (-2**15, -2**7, -2, -1, 0, 1, 2, 2**7-1, 2**15-1):
            self.assertEqual(self.foo.pack(v), self.foo.pack(long(v)))
            self.assertEqual(self.foo.pack(v), struct.pack('h', v))

        self.assertRaises(struct.error, self.foo.pack, -
