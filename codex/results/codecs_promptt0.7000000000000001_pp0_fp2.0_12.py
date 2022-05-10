import codecs
# Test codecs.register_error()
import string
# Test codecs.register()
import encodings
# Test encodings.search_function()
import encodings.utf_8
# Test encodings.utf_8.getregentry()
import encodings.iso8859_1
# Test encodings.iso8859_1.getregentry()
import encodings.ascii
# Test encodings.ascii.getregentry()
import encodings.latin_1
# Test encodings.latin_1.getregentry()
import test.test_support
import unittest
import sys


class CodecsTest(unittest.TestCase):

    def test_utf8(self):
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode,
            '\xff', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode,
            '\xfe', 'strict', True)
        self.assertRaises(Unicode
