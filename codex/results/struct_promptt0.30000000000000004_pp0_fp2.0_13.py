import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
import copy
import pickle
import test.support

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('i'*100), 400)
        self.assertEqual(_struct.calcsize('i'*1000), 4000)
        self.assertEqual(_struct.calcsize('i'*10000), 40000)

    def test_unpack_from(self):
        buf = b'abcd0123'
        self.assertEqual(_struct.unpack_from('4s4s', buf, 0), (b'abcd', b'0123'))
        self.assertEqual(_struct.unpack_from('4s4s', buf, 2), (b'cd01', b'23'))
        self.assertEqual(_struct
