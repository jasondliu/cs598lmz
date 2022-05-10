import lzma
lzma.LZMACompressor(format=lzma.FORMAT_RAW)
lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
lzma.LZMAFile(fileobj=None, mode='r', format=lzma.FORMAT_AUTO, check=-1, preset=None, filters=None)
lzma.open(filename, mode='r', format=lzma.FORMAT_AUTO, check=-1, preset=None, filters=None)
lzma.FILTER_LZMA1
lzma.FILTER_LZMA2
lzma.CHECK_NONE
lzma.CHECK_CRC32
lzma.CHECK_CRC64
lzma.CHECK_SHA256
lzma.FORMAT_AUTO
lzma.FORMAT_XZ
lzma.FORMAT_ALONE
lzma.FORMAT_RAW
lzma.is_check_supported(check)
lzma.CHECK_UNKNOWN
lzma.CHECK_ID_
