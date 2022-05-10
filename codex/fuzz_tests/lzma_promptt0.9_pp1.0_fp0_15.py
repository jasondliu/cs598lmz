import lzma
# Test LZMADecompressor against the reference implementation (lzma)

from string import ascii_letters
import random
import io
from sys import executable, version_info
import unittest

from test import support
from test.support import bigmemtest


# We are using lzma.LZMAFile to read the compressed streams and to uncompress
# them (round-trip).
from lzma import LZMAFile
from lzma import FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, CHECK_CRC32, CHECK_CRC64, CHECK_NONE
from lzma import FILTER_LZMA1, FILTER_LZMA2
from lzma import DECOMPRESS_OK, DECOMPRESS_DATA_ERROR, DECOMPRESS_FORMAT_ERROR


#
# Reading tests
#


class LZMAFileTestCaseRead(unittest.TestCase):
    mode = 'rb'
    level = 6
    # We need to have a small starting dictionary so that the incompressible
    # blocks are always the same length, regardless of the
