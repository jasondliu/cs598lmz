import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

# Import the base class for tested codec
from test_codecs import CodecSearchPathTestBase, CodecsMapTestBase

import encodings

# Import the base class for tested codec
from test_codecs import CodecSearchPathTestBase, CodecsMapTestBase

# Import the codecs module to be tested
import encodings

import sys
import unittest
import warnings

from test import support

# List of test cases

TESTCASES = [
    (b"abc\u20ac\u20ac\u20acdef", "latin-1", "latin-1"),
    (b"abc\xa4\xa4\xa4def", "latin-1", "latin-1"),
    (b"abcdef", "latin-1", "latin-1"),
    (b"abc\u20ac\u20ac\u20acdef", "ascii", "ascii", "replace"),
    (b"abc\xa4\xa4\xa4
