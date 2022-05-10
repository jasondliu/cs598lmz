import lzma
# Test LZMADecompressor, LZMACompressor, and LZMAFile
import warnings
import random
import struct
import io
import subprocess
import sys
import test.support
import unittest
import os
import os.path

try:
    from test import script_helper
except ImportError:
    # Python < 3.2
    from test.script_helper import assert_python_ok
    from test.script_helper import assert_python_failure


class LZMABytesIOTestCase(unittest.TestCase):
    compressed_text = open(
            os.path.join(os.path.dirname(__file__), "compressed.xz"),
            "rb").read()
    uncompressed_text = open(
            os.path.join(os.path.dirname(__file__), "uncompressed.txt"),
            "rb").read()
    def setUp(self):
        self.dec = lzma.LZMADecompressor()

    def test_unused_data(self):
        dec = self.dec
        self
