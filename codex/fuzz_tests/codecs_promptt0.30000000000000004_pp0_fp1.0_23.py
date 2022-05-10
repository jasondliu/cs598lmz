import codecs
# Test codecs.register_error

import test_support
import unittest

class CodecsTest(unittest.TestCase):

    def test_register_error(self):
        # Test the basic operation of the register_error function
        def bad_handler(exception):
            raise exception
        codecs.register_error("test.badhandler", bad_handler)
        self.assertEqual(codecs.lookup_error("test.badhandler"), bad_handler)
        self.assertRaises(UnicodeError, codecs.lookup_error, "test.unknown")

    def test_register_error_twice(self):
        # Test that registering twice raises a ValueError
        def bad_handler(exception):
            raise exception
        codecs.register_error("test.badhandler", bad_handler)
        self.assertRaises(ValueError, codecs.register_error,
                          "test.badhandler", bad_handler)

    def test_strict_errors(self):
        # Test the strict error handler
        self.assertRaises(UnicodeError, codec
