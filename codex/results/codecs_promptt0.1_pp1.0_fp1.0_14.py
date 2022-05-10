import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def my_error_handler(exception):
            return ("my_handler", len(exception.object))
        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        self.assertEqual(codecs.strict_errors, "strict")
        self.assertEqual(codecs.replace_errors, "replace")
        self.assertEqual(codecs.ignore_errors, "ignore")
        self.assertEqual(codecs.xmlcharrefreplace_errors, "xmlcharrefreplace")
        self.assertEqual(codecs.backslashreplace_errors, "backslashreplace")
        self.assertEqual(codecs.namereplace_errors, "namereplace")
        self.assertEqual
