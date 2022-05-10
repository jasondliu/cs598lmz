import lzma
# Test LZMADecompressor and LZMACompressor

from test import support
from test.support import bigmemtest
import unittest
from io import BytesIO, BufferedReader, BufferedWriter
from lzma import LZMADecompressor, LZMACompressor
from lzma import FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, CHECK_NONE, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256

TESTFN = support.TESTFN

class BaseTest:
    # Base class for LZMADecompressor and LZMACompressor tests.

    def setUp(self):
        self.decompressor = LZMADecompressor()
        self.compressor = LZMACompressor()
        self.fname = TESTFN

    def tearDown(self):
        support.unlink(self.fname)

    def test_invalid_args(self):
        # Test invalid constructor arguments.
        self.assertRaises(ValueError, self.decompressor.__init__, format=
