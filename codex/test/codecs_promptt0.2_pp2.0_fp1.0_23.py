import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # This test is not exhaustive, but it should cover the most common
        # cases.
        def handler(exception):
            return (u"", exception.end)

        codecs.register_error("test_error_handler", handler)
        self.assertEqual(codecs.lookup_error("test_error_handler"), handler)

        # Test that the error handler is actually used.
        self.assertEqual(u"abc".encode("ascii", "test_error_handler"), "abc")
        self.assertEqual(u"\u1234".encode("ascii", "test_error_handler"), "")

        # Test that the error handler is actually used with the
        # incremental encoder.
        encoder = codecs.getincrementalencoder("ascii")("test_error_handler")
        self.assertEqual(encoder.encode(u"abc"), "abc")
