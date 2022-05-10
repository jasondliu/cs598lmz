import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        codecs.register_error("test.strict", None)
        self.assertEqual(codecs.lookup_error("test.strict"), None)

    def test_bad_handler(self):
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.strict", handler)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", "foo")
        self.assertRaises(TypeError, codecs.register_error, "test.strict", 42)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", object())
