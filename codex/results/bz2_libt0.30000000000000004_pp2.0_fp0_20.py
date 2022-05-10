import bz2
bz2.decompress(bz2_data)

# gzip
import gzip
gzip_data = gzip.compress(orig_data)
gzip.decompress(gzip_data)

# lzma
import lzma
lzma_data = lzma.compress(orig_data)
lzma.decompress(lzma_data)

# zlib
import zlib
zlib_data = zlib.compress(orig_data)
zlib.decompress(zlib_data)

# zstandard
import zstandard
zstd_data = zstandard.ZstdCompressor().compress(orig_data)
zstandard.ZstdDecompressor().decompress(zstd_data)

# brotli
import brotli
brotli_data = brotli.compress(orig_data)
brotli.decompress(brotli_data)

# lz4
import lz4.frame
lz4_data = lz4.frame.compress(orig_
