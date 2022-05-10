import lzma
lzma.LZMACompressor()
lzma.LZMADecompressor()

# bz2
import bz2
bz2.BZ2Compressor()
bz2.BZ2Decompressor()

# zlib
import zlib
zlib.compress()
zlib.decompress()

# gzip
import gzip
gzip.compress()
gzip.decompress()

# lz4
import lz4
lz4.frame.compress()
lz4.frame.decompress()

# snappy
import snappy
snappy.compress()
snappy.decompress()

# brotli
import brotli
brotli.compress()
brotli.decompress()

# zstd
import zstd
zstd.compress()
zstd.decompress()

# blosc
import blosc
blosc.compress()
blosc.decompress()

# zopfli
import zopfli
zopfli.comp
