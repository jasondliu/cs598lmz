import _struct
# Test _struct.Struct.format_size()

import unittest
from test import support

class FormatSizeTestCase(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(_struct.Struct('i').format_size('<'), 4)
        self.assertEqual(_struct.Struct('i').format_size('>'), 4)
        self.assertEqual(_struct.Struct('i').format_size('!'), 4)
        self.assertEqual(_struct.Struct('b').format_size('<'), 1)
        self.assertEqual(_struct.Struct('b').format_size('>'), 1)
        self.assertEqual(_struct.Struct('b').format_size('!'), 1)
        self.assertEqual(_struct.Struct('h').format_size('<'), 2)
        self.assertEqual(_struct.Struct('h').format_size('>'), 2)
        self.assertEqual(_struct.Struct('h').format_size('!'), 2)
