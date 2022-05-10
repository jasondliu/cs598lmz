import _struct
# Test _struct.Struct
import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with test_support.check_py3k_warnings():
            self.assertEqual(_struct.calcsize('i'), 4)
            self.assertEqual(_struct.calcsize('ii'), 8)
            self.assertEqual(_struct.calcsize('i'*1000), 4000)
            self.assertEqual(_struct.calcsize('if'), 8)
            self.assertEqual(_struct.calcsize('ifh'), 12)
            self.assertEqual(_struct.calcsize('ifhhi'), 16)
            self.assertEqual(_struct.calcsize('ifhh'), 16)
            self.assertEqual(_struct.calcsize('ifhhd'), 24)
            self.assertEqual(_struct.calcsize('ifhhdP'), 24)
            self.assertEqual(_struct.calcsize('ifhhdPc'), 25)
