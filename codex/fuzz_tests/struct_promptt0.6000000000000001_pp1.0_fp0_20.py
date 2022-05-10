import _struct
# Test _struct.Struct
import unittest
from test import support

# Issue #17140: check that _struct.Struct works with non-ascii identifier chars.
class _TestStruct(unittest.TestCase):
    def test_nonascii_identifiers(self):
        # Test that _struct.Struct(<name>) works with non-ascii identifiers.
        # Test that Struct(<name>) works with non-ascii identifier.
        # Test that Struct(<name>).__name__ is bytes.
        for name in ('\u0393', '\u03A9', '\u03B3', '\u03B9'):
            struct = _struct.Struct(name)
            self.assertEqual(struct.__name__, name.encode('ascii'))
            self.assertEqual(struct.format, '=')
            self.assertEqual(struct.size, 0)
            self.assertEqual(struct.unpack(b''), ())
            self.assertEqual(struct.pack(()), b'')

        # Test that
