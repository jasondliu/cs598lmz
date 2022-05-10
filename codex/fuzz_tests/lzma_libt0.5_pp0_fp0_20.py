import lzma
lzma.LZMAError

from . import _lzma as lzma

import lzma.compress as compress
import lzma.decompress as decompress

import lzma.compressfile as compressfile
import lzma.decompressfile as decompressfile

import lzma.is_check_supported as is_check_supported
import lzma.CHECK_ID_MAX as CHECK_ID_MAX
import lzma.CHECK_ID_POWERPC as CHECK_ID_POWERPC
import lzma.CHECK_ID_CRC64 as CHECK_ID_CRC64
import lzma.CHECK_ID_SHA256 as CHECK_ID_SHA256
import lzma.CHECK_ID_NONE as CHECK_ID_NONE
import lzma.CHECK_ID_CRC32 as CHECK_ID_CRC32
import lzma.CHECK_ID_CRC32_C as CHECK_ID_CRC32_C
import lzma.CHECK_ID_SHA1 as CHECK_ID_
