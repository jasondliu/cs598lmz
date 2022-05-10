import codecs
# Test codecs.register_error()

# This test is not exhaustive, but it does test the
# most common cases.

import codecs
import sys
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test the basic operation of the API
        def handler(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u"\ufffd", exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.unicode_error", handler)
        self.assertEqual(u"\ufffd".encode("ascii", "test.unicode_error"),
                         "\xff")
        self.assertEqual(u"\u1234".encode("ascii", "test.unicode_error"),
                         "\xff34")
        self.assertRaises(TypeError,
                          u"\u1234".encode, "ascii", "test.unicode_error",
                          True)
