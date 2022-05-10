import _struct
# Test _struct.Struct.format_size()

import _struct
import unittest
from test import support

class FormatSizeTest(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(_struct.Struct('@').format_size(""), 0)
        self.assertEqual(_struct.Struct('@').format_size("0"), 0)
        self.assertEqual(_struct.Struct('@').format_size("00"), 0)
        self.assertEqual(_struct.Struct('@').format_size("000"), 0)
        self.assertEqual(_struct.Struct('@').format_size("0000"), 0)
        self.assertEqual(_struct.Struct('@').format_size("00000"), 0)
        self.assertEqual(_struct.Struct('@').format_size("000000"), 0)
        self.assertEqual(_struct.Struct('@').format_size("0000000"), 0)
        self.assertEqual(_struct.Struct('@').format_size("00000000"), 0)
