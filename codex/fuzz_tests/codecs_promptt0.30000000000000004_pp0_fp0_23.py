import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsTest(unittest.TestCase):

    def test_register_error(self):
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.notanencoding", handler)
        self.assertRaises(LookupError,
                          codecs.lookup, "test.notanencoding")
        self.assertRaises(LookupError,
                          codecs.lookup, "test.notanencoding")
        codecs.register_error("test.notanencoding", handler)
        self.assertRaises(LookupError,
                          codecs.lookup, "test.notanencoding")
        self.assertRaises(LookupError,
                          codecs.lookup, "test.notanencoding")

    def test_strict_errors(self):
        self.assertRaises(UnicodeDecodeError,
                          "abc".decode, "ascii", "strict")
        self.assert
