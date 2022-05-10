import lzma
# Test LZMADecompressor with various inputs.

import binascii

from test.support import run_unittest, run_doctest
from test.support import verbose
from test import support

import lzma
from lzma import LZMAError, LZMADecompressor


# Test data files are stored compressed in the liblzma test suite.
#   https://tukaani.org/xz/
# Each test case is a text file of the format:
#   # <comment>
#   <hexadecimal_data>
#   ...
#   <hexadecimal_data>
#   ---
#   <bytes>
#   ...
#   <bytes>
# The comment is just a readable string describing the test.
# Each hexadecimal_data is a line containing ASCII hexadecimal data.
# The "---" line separates the input data from the expected output data.
# The bytes lines are expected output data. The expected output is the
# concatenated bytes lines.
TEST_CASES = [
    'good-01.txt',

