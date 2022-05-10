import _struct
# Test _struct.Struct.format_map()

import test.support
import unittest

class FormatMapTests(unittest.TestCase):

    def test_basic(self):
        # Basic test from the docs
        s = _struct.Struct('h')
        self.assertEqual(s.format_map({'h': 'short'}), 'short')

    def test_missing_format(self):
        s = _struct.Struct('h')
        self.assertRaises(ValueError, s.format_map, {})

    def test_bad_format(self):
        s = _struct.Struct('h')
        self.assertRaises(ValueError, s.format_map, {'h': 'hort'})

    def test_override_format(self):
        # Test overriding a format
        s = _struct.Struct('h')
        self.assertEqual(s.format_map({'h': 'long'}), 'long')

    def test_override_format_size(self):
        # Test overriding a format with a different size
        s
