import lzma
# Test LZMADecompressor.

# This test has been adapted from test_lzma.py.

import unittest
from test import support

from io import BytesIO
from lzma import LZMADecompressor, LZMACompressor
from lzma import FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, CHECK_NONE, CHECK_CRC32
from lzma import CHECK_CRC64, CHECK_SHA256
from lzma import LZMAError, LZMAFile

# Example data from http://tukaani.org/xz/xz-file-format.txt
#
# The first two examples are XZ streams with a single Stream Header
# and a single Block, followed by the compressed data and the Index.
#
# The last example is a raw .lzma file with LZMA properties followed
# by the compressed data.

XZ_HEADER = b'\xfd7zXZ\x00'
XZ_FOOTER = b'YZ'
XZ_EXAMPLES = [

