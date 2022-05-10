import codecs
# Test codecs.register_error()
import re
import sys
import struct
import unittest
import warnings
from test import support

# The legacy C API is not available under PyPy
try:
    import _testcapi
except ImportError:
    _testcapi = None

# Some tests require the locale module
try:
    import locale
except ImportError:
    locale = None

class ErrorHandlingTestCase(unittest.TestCase):
    def test_bad_decode_args(self):
        self.assertRaises(TypeError, codecs.decode)
        self.assertRaises(TypeError, codecs.decode, 'abc')
        self.assertRaises(TypeError, codecs.decode, 'abc', 'utf-8', 42)
        self.assertRaises(TypeError, codecs.decode, 'abc', 'utf-8', 42,
                          42)

    def test_bad_encode_args(self):
        self.assertRaises(TypeError, codecs.encode)
        self.assertRaises(TypeError, codecs
