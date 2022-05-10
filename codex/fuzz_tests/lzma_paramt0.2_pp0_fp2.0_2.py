from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
bz2.decompress(compressed_data)

# zlib
import zlib
zlib.decompress(compressed_data)

# gzip
import gzip
gzip.decompress(compressed_data)

# brotli
import brotli
brotli.decompress(compressed_data)

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(compressed_data)

# lz4
import lz4.block
lz4.block.decompress(compressed_data)

# snappy
import snappy
snappy.uncompress(compressed_data)

# lzf
import lzf
lzf.decompress(compressed_data)

# lz4
import lz4
lz4.decompress(compressed_data)

# lz4framed
import lz4framed
lz4framed.dec
