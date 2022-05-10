import lzma
# Test LZMADecompressor

# Test the LZMADecompressor class

import unittest

from test import support

# Test data

# The test data is a list of tuples (compressed_data, uncompressed_data).
# The compressed data is a list of strings.  The decompressor is fed the
# compressed data one string at a time.  The uncompressed data is a single
# string.

test_data = [
    ([""], ""),
    (["\x00"], "\x00"),
    (["\x00\x00"], "\x00\x00"),
    (["\x00\x00\x00"], "\x00\x00\x00"),
    (["\x00\x00\x00\x00"], "\x00\x00\x00\x00"),
    (["\x00\x00\x00\x00\x00"], "\x00\x00\x00\x00\x00"),
    (["\x00\x00\x00\x00\x00\x00"], "\x00\x00
