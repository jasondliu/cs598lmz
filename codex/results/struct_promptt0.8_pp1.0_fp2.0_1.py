import _struct
# Test _struct.Struct.__repr__ and _struct.__getitem__.

import test.test_support
import unittest

class StructTest(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(_struct.Struct('h')), 'Struct("h")')
        self.assertEqual(repr(_struct.Struct('x')), 'Struct("x")')
        self.assertEqual(repr(_struct.Struct('b')), 'Struct("b")')
        self.assertEqual(repr(_struct.Struct('bbbb')), 'Struct("bbbb")')
        self.assertEqual(repr(_struct.Struct('4h')), 'Struct("4h")')
        self.assertEqual(repr(_struct.Struct('hhh')), 'Struct("hhh")')
        self.assertEqual(repr(_struct.Struct('1024s')), 'Struct("1024s")')
        self.assertEqual(repr(_struct.Struct('f')), 'Struct("f")')
        self.assertEqual(
