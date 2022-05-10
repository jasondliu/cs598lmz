import _struct
# Test _struct.Struct
from test import test_support
import unittest
from binascii import hexlify

class StructTestCase(unittest.TestCase):

    def test_format_sizeof(self):
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('=i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('<i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('>i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('!i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('=ih'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('!ih'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('<ih'))
