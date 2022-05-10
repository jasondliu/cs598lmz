import bz2
# Test BZ2Decompressor, BZ2Compressor
import copy
from test import support
from test.support import TESTFN, run_unittest
import unittest
from io import BytesIO
import itertools
import os
from random import randint
from bz2file import BZ2File


# The block size of bz2.BZ2Decompressor, bz2.BZ2Compressor, bz2file.BZ2File
# and the bz2 C library is 9.
BZ2_BLOCKSIZE = 9
BZ2_WORKFACTOR = 30
BZ2_BUFFER_SIZE = 8192

# Adapted from http://www.bzip.org/1.0.3/html/bzip2-manual-1.0.3.html#crash-recovery
# The first file has a random number of blocks. The second file has a
# random number of blocks, plus one more. In other words, it's missing
# the last block. The third file has the same number of blocks and
# the same content as the second file. The last block of
