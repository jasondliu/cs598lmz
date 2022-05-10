import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering a new error handler
        def handler(exception):
            return (u'', exception.start + 1)
        codecs.register_error("test.my_error_handler", handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"), handler)

    def test_register_error_twice(self):
        # Test registering a new error handler twice
        def handler(exception):
            return (u'', exception.start + 1)
        codecs.register_error("test.my_error_handler", handler)
        self.assertRaises(KeyError, codecs.register_error,
                          "test.my_error_handler", handler)

    def test_register_error_invalid_name(self):
        # Test registering an error handler with an invalid name
        def handler(exception):
            return (u'', exception.start + 1
