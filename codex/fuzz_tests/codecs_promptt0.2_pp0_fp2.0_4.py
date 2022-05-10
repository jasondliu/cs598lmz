import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error("test.lookup", handler)
        # Test that the error handler is used
        self.assertEqual(u"abc".encode("test.lookup", "test.lookup"),
                         (u"abc", 3))
        # Test that the error handler is used for the right category
        self.assertRaises(LookupError, u"abc".encode, "test.lookup", "strict")
        # Test that the error handler is used for the right encoding
        self.assertRaises(LookupError, u"abc".encode, "ascii", "test.lookup")
        # Test that the error handler is used for the right encoding
        # and category
        self.assertEqual(u"abc".encode("ascii", "test.lookup"),

