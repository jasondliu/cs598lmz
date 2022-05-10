import codecs
# Test codecs.register_error()

# This test is a modified version of test_codecs.py

import codecs
import os
import sys
import unittest
import warnings
import string
import tempfile

try:
    from test import support
except ImportError:
    from test import test_support as support

# Decoding

class CodecTest(unittest.TestCase):
    def test_basics(self):
        for encoding in ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'iso-8859-1']:
            for errors in ['strict', 'replace', 'ignore']:
                assert codecs.decode(b'\xff', encoding, errors) == codecs.decode(b'\xff', encoding, errors)
                assert codecs.decode(b'\xff', encoding, errors) == codecs.decode(b'\xff', encoding, errors)
                assert codecs.decode(b'\xff', encoding, errors) == codecs.decode(b'\xff', encoding, errors)
               
