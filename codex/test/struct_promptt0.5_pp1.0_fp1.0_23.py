import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # test a number of standard formats
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iH'), 6)
        self.assertEqual(_struct.calcsize('iHh'), 8)
        self.assertEqual(_struct.calcsize('iHHHH'), 16)
        self.assertEqual(_struct.calcsize('iHHHHh'), 18)
        self.assertEqual(_struct.calcsize('iHHHHhH'), 20)
        self.assertEqual(_struct.calcsize('iHHHHhHH'), 22)
        self.assertEqual(_struct.calcsize('iHHHHhHHH'), 24)
        self.assertEqual(_struct.calcsize('iHHHHhHHHH'), 26)
