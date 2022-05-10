from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO)
from lzma import LZMACompressor
LZMACompressor(format=FORMAT_AUTO)
from lzma import open
open(filename, mode="r", format=None, check=-1, preset=None, filters=None)
from lzma import compress
compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
from lzma import decompress
decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)
from lzma import is_check_supported
is_check_supported(check)
from lzma import CHECK_NONE
from lzma import CHECK_CRC32
from lzma import CHECK_CRC64
from lzma import CHECK_SHA256
from lzma import FORMAT_AUTO
from lzma import FORMAT_XZ
from lzma import FORMAT_ALONE
from lzma import FORMAT_RAW
from lzma import FILTER_LZMA1
from
