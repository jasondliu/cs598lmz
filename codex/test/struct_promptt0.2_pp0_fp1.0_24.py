import _struct
# Test _struct.Struct.__getitem__

import unittest
from test import support

class GetItemTest(unittest.TestCase):

    def test_getitem(self):
        s = _struct.Struct('i')
        self.assertEqual(s[0], 'i')
        self.assertEqual(s[1], 'i')
        self.assertEqual(s[-1], 'i')
        self.assertEqual(s[-2], 'i')
        self.assertRaises(IndexError, s.__getitem__, 2)
        self.assertRaises(IndexError, s.__getitem__, -3)

    def test_getitem_format(self):
        s = _struct.Struct('ii')
        self.assertEqual(s[0], 'i')
        self.assertEqual(s[1], 'i')
        self.assertEqual(s[-1], 'i')
        self.assertEqual(s[-2], 'i')
