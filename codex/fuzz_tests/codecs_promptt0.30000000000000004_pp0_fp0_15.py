import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error()
        def handler(exception):
            return ("xyz", exception.start + 3)
        codecs.register_error("test.my_error_handler", handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"), handler)
        codecs.register_error("test.my_error_handler", None)
        self.assertRaises(LookupError, codecs.lookup_error, "test.my_error_handler")

    def test_lookup_error(self):
        # Test codecs.lookup_error()
        self.assertEqual(codecs.lookup_error("strict"), codecs.strict_errors)
        self.assertEqual(codecs.lookup_error("ignore"), codecs.ignore_errors)
        self.assertEqual(codecs.lookup_error
