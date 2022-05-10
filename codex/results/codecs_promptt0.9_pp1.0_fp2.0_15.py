import codecs
# Test codecs.register_error("ignore", "", "")....
import os
import struct
import sys
from test import test_support
import unittest
import unicodedata
import warnings

# None of these tests actually look at the file contents, so they should all
# work with any valid file, not just the ones in the test data directory.
test_file_content = test_support.findfile("testdata", "readline.h")

test_text = "a\n"
test_text_readlines = test_text.split("\n")

test_binary_len = os.stat(test_file_content).st_size


class TestUniversalNewline(unittest.TestCase):
    def setUp(self):
        if sys.platform == "darwin":
            self.lfonly = test_support.findfile("testdata", "lfonly.txt")

    def tearDown(self):
        pass

    def test_returned_lines(self):
        # Test that readline(), read(), readlines(), and file iterators
        # return lines with newlines intact"
        for
