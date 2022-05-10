import codecs
# Test codecs.register_error

# This test is not exhaustive, but it should catch most of the
# problems.

# The tests are run twice: once with the default 'strict' error
# handler, and once with a custom 'ignore' error handler.

# The custom error handler is necessary to test the error handler
# registration mechanism.

import codecs
import unittest

from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        def bad_handler(exception):
            raise RuntimeError("bad handler")
        def good_handler(exception):
            return ("", 0)
        def bad_handler2(exception):
            return ("", 0, 0)
        def bad_handler3(exception):
            return ("", 0, 1)
        def bad_handler4(exception):
            return ("", 0, 1, 2)
        def bad_handler5(exception):
            return ("", 0, 1, 2, 3)
        def bad_handler6(ex
