import codecs
# Test codecs.register_error

# This test is for the codecs module.

import codecs
import unittest
import sys
import test.support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        def bad_handler(exception):
            raise RuntimeError("bad_handler called")
        self.assertRaises(RuntimeError, codecs.register_error,
                          "bad_handler", bad_handler)
        self.assertRaises(LookupError, codecs.register_error,
                          "bad_handler", None)
        self.assertRaises(LookupError, codecs.register_error,
                          "bad_handler", "not callable")
        self.assertRaises(LookupError, codecs.register_error,
                          "bad_handler", lambda x: x)
        self.assertRaises(LookupError, codecs.register_error,
                          "bad_handler", lambda x, y: x)
        self.assertRaises(LookupError, codecs
