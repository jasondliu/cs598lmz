import codecs
# Test codecs.register_error("test_name", test_method)

import struct
import sys

import unittest
from test import support

def _make_test_str():
    # Create a test string which consists of all characters below the maximum
    # unicode code point plus blank characters in between.
    test_str = ""
    # Maximum code point using 16 bits.
    MAX_UNICODE = 0xFFFF
    # Increment to get spaces in between.
    INCREMENT = 0x500
    for char in range(0, MAX_UNICODE + INCREMENT, INCREMENT):
        test_str = test_str + chr(char)
    return test_str

def _is_jython():
    return sys.platform.startswith("java")

class IncrementalEncoderTest(unittest.TestCase):

    def test_bug2613(self):
        from codecs import getincrementalencoder
        nl = "\n".encode("ascii")
        encoder = getincrementalencoder("utf-16")()
        self.assertEqual
