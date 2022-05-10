from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

from lzma import open
open(filename, mode='r', format=FORMAT_AUTO, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

from lzma import compress
compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)

from lzma import decompress
decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

from lzma import FILTER_LZMA2
FILTER_LZMA2(id=33, preset=None, flags=0)

from lzma import FILTER_DELTA
FILTER_DELTA(dist=1)

from lzma import FILTER_X86
FILTER_X86(id=38)

from lzma import FILTER_IA64
FILTER_IA64(id=39)

from lzma import FILTER_ARM
FILTER_
