from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.decompress()
import lzma
lzma.decompress(data)

# bz2.decompress()
import bz2
bz2.decompress(data)

# zlib.decompress()
import zlib
zlib.decompress(data)

# gzip.decompress()
import gzip
gzip.decompress(data)

# lz4.block.decompress()
import lz4.block
lz4.block.decompress(data)

# blosc.decompress()
import blosc
blosc.decompress(data)

# brotli.decompress()
import brotli
brotli.decompress(data)

# snappy.decompress()
import snappy
snappy.decompress(data)

# zstd.decompress()
import zstd
zstd.decompress(data)

# lzma.open()
import lzma

