from _struct import Struct
s = Struct.__new__(Struct)
reload(struct)

import unittest
from test import test_support
import sys

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(struct.calcsize(""), 0)
        self.assertEqual(struct.calcsize("<"), 0)
        self.assertEqual(struct.calcsize("< "), 0)
        self.assertEqual(struct.calcsize(" <"), 0)
        self.assertEqual(struct.calcsize("<>"), 0)
        self.assertEqual(struct.calcsize("<1"), 0)
        self.assertEqual(struct.calcsize("<1s"), 1)
        self.assertEqual(struct.calcsize("<256s"), 256)
        self.assertEqual(struct.calcsize("<256s", 256), 256)
        self.assertEqual(struct.calcsize("<h"), 2)
        self.assertEqual(struct.calcsize("<i"),
