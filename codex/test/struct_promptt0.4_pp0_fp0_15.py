import _struct
# Test _struct.Struct
import unittest
from test import support
from test.support import import_helper

_struct = import_helper.import_module('_struct')

class StructTestCase(unittest.TestCase):

    def test_unpack(self):
        self.assertEqual(_struct.unpack('i', b'abcd'), (1633837924,))
        self.assertEqual(_struct.unpack('h', b'abcd'), (25185,))
        self.assertEqual(_struct.unpack('hh', b'abcd'), (25185, 43777))
        self.assertEqual(_struct.unpack('hh', b'ab'), (25185,))

    def test_unpack_from(self):
        self.assertEqual(_struct.unpack_from('i', b'abcd'), (1633837924,))
        self.assertEqual(_struct.unpack_from('h', b'abcd'), (25185,))
