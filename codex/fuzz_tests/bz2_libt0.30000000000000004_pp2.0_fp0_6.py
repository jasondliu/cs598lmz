import bz2
bz2.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# lz4
import lz4.frame
lz4.frame.decompress(data)

# snappy
import snappy
snappy.decompress(data)

# zstandard
import zstandard
zstandard.ZstdDecompressor().decompress(data)

# blosc
import blosc
blosc.decompress(data)

# lzf
import lzf
lzf.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# lz4
import lz4
lz4.decompress(data)

# lz4
import lz4
