import lzma
lzma.FILTER_X86

from lzma import LZMACompressor, LZMADecompressor
from lzma import FORMAT_ALONE, FORMAT_XZ
from lzma import CHECK_CRC32, CHECK_CRC64, CHECK_SHA256

import shutil

