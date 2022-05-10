import codecs
# Test codecs.register_error()
from test import support
support.import_module('unicodedata')
import unicodedata
import unittest
import io


class ErrorHandlingTest(unittest.TestCase):
    def test_decode(self):
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode,
            b'\x80', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode,
            b'+AAA-', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode,
            b'+\x80-', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode,
            b'+--\x80', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode,
            b'+A\x80A-', 'strict
