import codecs
# Test codecs.register_error

# This test is not exhaustive, but it should catch most of the problems.

# The error handler is called with the following arguments:
# (exception object, encoding, string, startindex, endindex)
# It should return a (replacement, newindex) tuple, with newindex the
# same as the endindex by default.

# The error handler is called until it either returns a string ending
# before the endindex, or raises an exception.

# The error handler is also called for encoding errors.

# The error handler is also called for character to byte encoding
# errors.

# The error handler is also called for character to byte encoding
# errors.

import codecs
import sys
import unittest

class Test_register_error(unittest.TestCase):
    def test_register_error(self):
        def bad_handler(exception, encoding, string, start, end):
            raise ValueError
        codecs.register_error("test.bad_handler", bad_handler)
        self.assertRaises(ValueError, codecs.lookup_error, "
