import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# Tests for various errors and exceptions in Unicode C APIs

# test buffer interface

import _testcapi

import unittest
from test import support

class UnicodeErrorTest(unittest.TestCase):

    def test_returncodes(self):
        # Map return codes to exception classes
        class_ = KeyError
        for code in (120, 121, 122,
                     123, 124, 125, 126, 127,
                     128, 129, 130, 131):
            self.assertIs(class_, _testcapi.unicode_error_class(code))
        for code in range(132, 256):
            self.assertIs(UnicodeError, _testcapi.unicode_error_class(code))

    def test_buffer(self):
        # Map UnicodeErrors to return codes
        class_ = KeyError
        buffer = "abcd"
        for code in (120, 121, 122,
                     123, 124, 125, 126, 127,
                     128, 129, 130, 131):
            self.assertEqual(
                code,
                _
