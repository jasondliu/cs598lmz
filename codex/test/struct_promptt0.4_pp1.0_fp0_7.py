import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_format_sizeof_alignment(self):
        # Test _struct.Struct format, sizeof, and alignment.
        # See http://docs.python.org/library/struct.html#format-characters
        # for more details.
        #
        # The following macros are used to test format, sizeof, and alignment
        # of _struct.Struct objects.
        def check_sizeof_alignment(format, expected_size, expected_alignment):
            s = _struct.Struct(format)
            self.assertEqual(s.size, expected_size)
            self.assertEqual(s.alignment, expected_alignment)

        # The 'x' format character is used to skip bytes.
        check_sizeof_alignment('x', 1, 1)
        check_sizeof_alignment('xx', 2, 1)
        check_sizeof_alignment('xxx', 3, 1)

        # The 'c' format character is used to represent
