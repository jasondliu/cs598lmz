from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# lzma
# Compress data in one shot and return the compressed string.
import lzma
lzma.compress(data)

# bz2
# bz2.compress(data)
# bz2.decompress(data)
import bz2
bz2.compress(data)

# zlib
# zlib.compress(data, level=9)
# zlib.decompress(data)
import zlib
zlib.compress(data)

# brotli
# brotli.compress(data, mode=MODE_GENERIC, quality=11, lgwin=22)
# brotli.decompress(data)
import brotli
brotli.compress(data)

# zstandard
# zstd.compress(data, level=3)
# zstd.decompress(data)
import zstd
zstd.compress(data)

# blosc
# blosc.compress(data, typesize=8)
#
