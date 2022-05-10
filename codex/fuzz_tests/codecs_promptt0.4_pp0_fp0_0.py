import codecs
# Test codecs.register_error
#
# This test is intended to verify that the register_error() function
# works as intended.

import codecs
import unittest
from test import support

# This class is used to test the handling of codec errors
class Codec_Error:
    def __init__(self, encoding):
        self.encoding = encoding

    def __call__(self, error):
        if isinstance(error, UnicodeDecodeError):
            return ("", error.end)
        else:
            return ("", 1)

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test the register_error() function
        #
        # This test verifies that the register_error() function works
        # as intended.

        # Test 1: Verify that the error handler can be registered
        codecs.register_error("strict", Codec_Error("strict"))

        # Test 2: Verify that the error handler can be retrieved
        error = codecs.lookup_error("strict")
        self.assertEqual(error.encoding,
