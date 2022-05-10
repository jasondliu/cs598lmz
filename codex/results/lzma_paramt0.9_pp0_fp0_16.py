from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, memlimit=MEMLIMIT)

from lzma import open
open(filename, mode="w", format=FORMAT_RAW, check=-1, preset=None, filters=None)

from lzma import IsLZMACompatible
IsLZMACompatible(data)

from lzma import CFCHECK_CRC32
from lzma import CFCHECK_CRC64
from lzma import CFCHECK_SHA256

import os
from lzma import CHECK_NONE
from lzma import CHECK_CRC32
from lzma import CHECK_CRC64
from lzma import CHECK_SHA256

from lzma import FILTER_DELTA
from lzma import FILTER_LZMA1
from lzma import FILTER_LZMA2
from lzma import FILTER_X86
from lzma import FILTER_IA64
from lzma import FILTER_ARM
from lzma import FILTER_ARMTHUMB
from lzma import FILTER_P
