import codecs
# Test codecs.register_error()

# This test is not complete.  It is only meant to test the
# functionality of the codecs.register_error() function.

import codecs
import unittest
from test import test_support

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test the functionality of the register_error() function.
        #
        # The function should take a name, an error handler, and
        # optionally a flag indicating whether the error handler is
        # to be used for encoding or decoding.  If the flag is not
        # given, the error handler should be used for both encoding
        # and decoding.
        #
        # The error handler should be called with the exception
        # instance, the encoding or decoding name, and the input
        # string.  The error handler should return a tuple of the
        # replacement string and the number of characters to skip.
        #
        # The error handler should be used when the codec encounters
        # an error.  The codec should use the error handler to
        # determine the replacement string and the number of

