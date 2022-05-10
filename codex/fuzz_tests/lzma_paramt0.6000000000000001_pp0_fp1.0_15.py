from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

from lzma import open as lzopen
lzopen(filename=None, mode='r', format=FORMAT_AUTO, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

from lzma import open_stream
open_stream(file_obj=None, mode='r', format=FORMAT_AUTO, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

from lzma import compress
compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)

from lzma import decompress
decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

from lzma import is_check_supported
is_check_supported(check)

from lzma import CHECK_NONE
CHECK_NONE

from lzma import CHECK_CRC32
CHECK_C
