import lzma
# Test LZMADecompressor.

import unittest
import io
import os
import struct
import sys
import tempfile
import time
import warnings
import zlib

from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Skip test if the implementation is C version.
lzma = import_module('lzma')
if not hasattr(lzma, 'LZMADecompressor'):
    raise unittest.SkipTest("no LZMADecompressor implementation to test")

# Use the Python implementation of LZMACompressor.
LZMACompressor = lzma.LZMACompressor

# The test data was compressed with the following options:
# xz --format=raw -1 -c data.bin > data.xz
TEST_DATA = b"".join(struct.pack(">f", (i/3.0)) for i in range(0, 10000))
TEST_DATA_XZ = (
    b'\xfd7zXZ\x00\x00\x04\xe
