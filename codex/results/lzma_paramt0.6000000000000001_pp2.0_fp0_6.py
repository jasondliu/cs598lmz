from lzma import LZMADecompressor
LZMADecompressor().decompress(zlib.compress(b'Hello World!'))

# zlib.compress(data, level)
# zlib.decompress(data)

# lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
# lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

# lzma.LZMADecompressor.decompress(data, max_length=None)
# lzma.LZMADecompressor.flush(length=None)

# zlib.crc32(data[, value])
# zlib.adler32(data[, value])

# zlib.compress(data, level)
# zlib.decompress(data)

# lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
# lzma.decompress(data, format=FORMAT_AUTO, memlimit
