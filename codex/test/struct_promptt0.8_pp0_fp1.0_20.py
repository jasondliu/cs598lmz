import _struct
# Test _struct.Struct

import struct
import unittest
from test import support

try:
    import locale
    locale.setlocale(locale.LC_NUMERIC, 'German_Germany')
    has_german_locale = True
except locale.Error:
    has_german_locale = False

class FormatTestCase(unittest.TestCase):
    # Format to use for testing.
    format = None

    # Size in bytes of format
    size = None

    # Example (width, format, input, output)
    examples = ()

    def test_format_size(self):
        self.assertEqual(self.struct.size, self.size)

    def test_itemsize(self):
        self.assertEqual(self.struct.itemsize, self.size)

    def test_names(self):
        self.assertEqual(self.struct.names, None)

