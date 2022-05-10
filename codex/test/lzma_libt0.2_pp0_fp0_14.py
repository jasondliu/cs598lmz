import lzma
lzma.decompress(lzma.compress(b'Hello World'))

# b'Hello World'

# lzma.LZMADecompressor()
# lzma.LZMACompressor()

# lzma.open(filename, mode='rb', format=None, check=-1, preset=None, filters=None)
# lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
# lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

# lzma.FORMAT_XZ
# lzma.FORMAT_ALONE
# lzma.FORMAT_RAW
# lzma.CHECK_NONE
# lzma.CHECK_CRC32
# lzma.CHECK_CRC64
# lzma.CHECK_SHA256

# lzma.FILTER_LZMA1
# lzma.FILTER_LZMA2
# lzma.FILTER
