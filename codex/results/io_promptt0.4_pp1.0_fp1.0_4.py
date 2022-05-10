import io
# Test io.RawIOBase
import os
import sys
import tempfile
import unittest
from test import support
from test.support import TESTFN, run_unittest

# The tests in this suite are designed to be run with a variety of buffer
# sizes, to ensure that the RawIOBase implementations don't make invalid
# assumptions about buffer sizes.

# The default buffer size to use.
BUFSIZE = 8

# A sequence of buffer sizes to test.
BUFSIZES = (1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 63, 64, 65,
            127, 128, 129, 255, 256, 257, 32767, 32768, 32769, 65535, 65536,
            65537)

# A sequence of "arbitrary" (read: randomly generated) buffer sizes to test.
RANDOM_BUFSIZES = (
    16384, 22937, 62483, 46722, 54933, 61608, 23173, 54477,
    42459, 52428, 64447, 54917, 63491
