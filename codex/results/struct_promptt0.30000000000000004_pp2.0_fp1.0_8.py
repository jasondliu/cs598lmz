import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import test_support

# Test _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_format(self):
        # Test format string
        self.assertEqual(_struct.Struct('i').format, 'i')
        self.assertEqual(_struct.Struct('ii').format, 'ii')
        self.assertEqual(_struct.Struct('hi').format, 'hi')
        self.assertEqual(_struct.Struct('lh').format, 'lh')
        self.assertEqual(_struct.Struct('llh').format, 'llh')
        self.assertEqual(_struct.Struct('qh').format, 'qh')
        self.assertEqual(_struct.Struct('qqh').format, 'qqh')
        self.assertEqual(_struct.Struct('fd').format, 'fd')
        self.assertEqual(_struct.Struct('df').format, 'df')
        self.assertEqual(_struct.Struct('fd').format, 'fd')

