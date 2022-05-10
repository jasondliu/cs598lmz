import codecs
# Test codecs.register_error
import sys
import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Make sure we can register new error handlers
        def replace_handler(exc):
            if not isinstance(exc, UnicodeDecodeError):
                raise TypeError("don't know how to handle %r" % exc)
            return (u'\ufffd', exc.end)
        codecs.register_error("test.replace", replace_handler)
        self.assertEqual(codecs.lookup_error("test.replace"),
                         replace_handler)

    def test_lookup_unknown(self):
        # Make sure we get a sensible error for unknown error handlers
        self.assertRaises(LookupError,
                          codecs.lookup_error, "__made_up_error_name__")

    def test_strict_errors(self):
        # Test the 'strict' error handler
        self.assertRaises(UnicodeDecodeError,
                          '\xff'.decode
