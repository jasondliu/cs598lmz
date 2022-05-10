import bz2
# Test BZ2Decompressor
#
# This tests the decompressor itself, not the BZ2Decompressor class
#
# This test is based on bz2_file_test.py from the Python 2.5.2 standard library

import binascii
import struct
import sys
import zlib

from test import support

# The test data consists of a series of blocks, each of which is
# preceded by a 3-byte header:
#
#   0..1  Uncompressed size (little-endian)
#   2     Compression method (0-3)
#
# Followed by the block data itself.  Blocks are concatenated to
# form a single stream.  The first block has an uncompressed size of
# 0, and is followed immediately by the second block.  The second
# block has an uncompressed size of 0, and is followed immediately
# by the third block.  Etc.

# The compression methods used are:
#
#   0    Uncompressed
#   1    BZ_RLE
#   2    BZ_HUFFMAN_ONLY
#   3   
