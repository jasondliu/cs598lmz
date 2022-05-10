import codecs
# Test codecs.register_error
# -*- coding: latin-1 -*-
# Test the 'decode' an 'encode' methods of the unicode class.
# The error handling is tested by forcing a UnicodeError exception.
# Error handling should be done as follows :
# - the problematic character is replaced by an xml character reference
#   or by a question mark
# - a log line is printed, to inform the user about the problem
# - the exception is not raised
import codecs
import os
import sys
import unittest

class TestUnicodeMethods(unittest.TestCase):
    def test_encode_decode(self):
        s = u'\xfcbrigens'
        self.assertEqual(codecs.latin_1_encode(s), ('\xfcbrigens', 10))
        self.assertEqual(codecs.latin_1_decode('\xfcbrigens'), (s, 10))

