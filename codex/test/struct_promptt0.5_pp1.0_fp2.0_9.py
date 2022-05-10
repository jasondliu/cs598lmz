import _struct
# Test _struct.Struct.format
#
# The format string is checked for validity when the Struct object is created.
# Invalid format strings should raise ValueError.
#
# Passing a bad format string when creating a Struct should raise ValueError.

import _struct as struct
import unittest
import sys

class StructTest(unittest.TestCase):

    def test_format(self):
        # Test format string for validity
        self.assertRaises(ValueError, struct.Struct, 'x')
        self.assertRaises(ValueError, struct.Struct, 'cx')
        self.assertRaises(ValueError, struct.Struct, 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
        self.assertRaises(ValueError, struct.Struct, 'p')
        self.assertRaises(ValueError, struct.Struct, 'P')

        # Test format string with '@' alignment
        self.assertRaises(ValueError, struct.Struct, '@')
