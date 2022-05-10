from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bzip2
import bz2
bz2.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# zstandard
import zstandard
zstd_ctx = zstandard.ZstdDecompressor()
zstd_ctx.decompress(data)

# snappy
import snappy
snappy.uncompress(data)

# lz4
import lz4
lz4.block.decompress(data)

# lz4.frame
import lz4.frame
lz4.frame.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# zopfli
import zopfli
zopfli.decompress(data)

# zopfli.decompress
import zopfli
zopfli.decompress(data)

# zopfli.gzip
import zopfli
zopfli.gzip.
