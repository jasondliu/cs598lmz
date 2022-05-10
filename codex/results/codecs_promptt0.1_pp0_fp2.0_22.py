import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        # Test registering an error handler with a name
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.strict", handler, "strict")
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        self.assertEqual(codecs.lookup_error("strict"), handler)
        # Test registering an error handler with a name and an extra argument
        def handler(exception, encoding):
            return ("", exception.end)
        codecs.register_error("test.strict", handler, "strict", "utf-8")
       
