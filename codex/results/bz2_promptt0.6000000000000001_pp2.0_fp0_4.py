import bz2
# Test BZ2Decompressor with a single-byte read() call

# This test is based on test_bz2.BZ2Compressor.test_single_byte_read()
# from the Python 2.7.10 standard library test suite.

# The original test used a StringIO as the input source, which is not
# available in Python 3.
# Instead, we use a BytesIO.

from io import BytesIO
from bz2 import BZ2Decompressor
from test.support import run_unittest, TESTFN
import unittest

class TestBZ2Decompressor(unittest.TestCase):

    def test_single_byte_read(self):
        # Test BZ2Decompressor with a single-byte read() call.
        for compressed, uncompressed in (('BZh91AY&SY.1G\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff',
                                          'BZh91AY&SY\x19\x80P\x81\x11\x00\
