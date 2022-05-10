import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error()
        def handler(exception):
            return ("", 0)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "__builtin__.blah")
        self.assertRaises(TypeError, codecs.register_error, "test.strict", None)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", "blah")
        self.assertRaises(TypeError, codecs.register_error, "test.strict", 1)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", 1, 2, 3)
        self.assertRaises(TypeError, codecs.register
