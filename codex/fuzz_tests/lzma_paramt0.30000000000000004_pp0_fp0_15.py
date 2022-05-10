from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# zlib
import zlib
zlib.decompress(data)

# bz2
import bz2
bz2.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(data)

# snappy
import snappy
snappy.decompress(data)

# lz4
import lz4
lz4.block.decompress(data)

# lz4framed
import lz4.frame
lz4.frame.decompress(data)

# lz4json
import lz4.block
lz4.block.decompress(data)

# lz4msgpack
import lz4.frame
lz4.frame.
