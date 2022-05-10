import codecs
# Test codecs.register_error()
import re
import sys
import unittest
import warnings
from test import test_support

# Some codecs (e.g. UTF-7) don't do well with the default test string.
TESTSTRING = u"\u3042\u3044\u3046\u3048\u304a"

# Encodings that don't support the default test string
NON_STRING_ENCODINGS = ["ascii", "idna", "punycode", "string_escape",
                        "raw_unicode_escape", "unicode_escape", "uu_codec"]

class CodecsModuleTest(unittest.TestCase):

    def test_lookup(self):
        # lookup()
        self.assertEqual(codecs.lookup("string-escape"),
                         codecs.lookup("string_escape"))
        self.assertEqual(codecs.lookup("unicode-escape"),
                         codecs.lookup("unicode_escape"))
        self.assertEqual(codecs.lookup("string-escape").
