import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test registering a new error handler
        def my_error_handler(exception):
            return ("my_handler", exception.end)
        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        # Test registering an existing error handler
        def my_error_handler2(exception):
            return ("my_handler2", exception.end)
        codecs.register_error("test.my_error_handler", my_error_handler2)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler2)
        # Test registering an existing error handler with replace=False
