import _struct
# Test _struct.Struct
import array
import io
import sys
import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # All struct format characters are tested here.
        # The test results are taken from the C struct module's tests.
        # The '=' is for native byte ordering.
        formats = 'xcbBhHiIlLqQfdspP'
        native_fmts = '=' + formats
        standard_fmts = '@' + formats
        byte_orderings = ['@', '=', '<', '>', '!']
        alignment = [0, 1, 2, 4]
        for byte_ordering in byte_orderings:
            for alignment_setting in alignment:
                for format in native_fmts:
                    try:
                        struct.calcsize(byte_ordering + format)
                    except struct.error:
                        # Skip tests that are not applicable
                        pass
                    else:
                        break
                else:
                    # No valid format found, skip this alignment setting
                    continue
                break

