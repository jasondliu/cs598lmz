import codecs
# Test codecs.register_error()

import codecs
import unittest
import sys

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        def my_error_handler(exception):
            return (b'x', exception.end)
        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        self.assertEqual(codecs.strict_errors, "strict")
        self.assertEqual(codecs.replace_errors, "replace")
        self.assertEqual(codecs.ignore_errors, "ignore")
        self.assertEqual(codecs.xmlcharrefreplace_errors, "xmlcharrefreplace")
        self.assertEqual(codecs.backslashreplace_errors, "backslashreplace")
        self.assertEqual(codecs.namereplace_errors
