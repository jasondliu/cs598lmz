import codecs
# Test codecs.register_error() with "surrogateescape" error handler.
# See issue #10100

import sys
import unittest
from test import support

class SurrogateEscapeTest(unittest.TestCase):
    def test_surrogateescape(self):
        if sys.maxunicode == 65535:
            self.skipTest('need a UCS4 build')
        # Encode non-BMP characters with "surrogateescape".
        # We use a list of non-BMP characters instead of
        # unicode_escape to avoid adding more test dependencies.
        non_bmp = [
            0x10000, 0x10001, 0x10002, 0x10003, 0x10004, 0x10005, 0x10006,
            0x10007, 0x10008, 0x10009, 0x1000A, 0x1000B, 0x1000D, 0x1000E,
            0x1000F, 0x10010, 0x10011, 0x10012, 0x10013, 0x10014, 0x10015,
            0x100
