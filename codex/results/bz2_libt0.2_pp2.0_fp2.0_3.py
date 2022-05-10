import bz2
bz2.decompress(bz2_data)

# gzip
import gzip
gzip.decompress(gzip_data)

# lzma
import lzma
lzma.decompress(lzma_data)

# zlib
import zlib
zlib.decompress(zlib_data)

# brotli
import brotli
brotli.decompress(brotli_data)

# lz4
import lz4.frame
lz4.frame.decompress(lz4_data)

# lzf
import lzf
lzf.decompress(lzf_data)

# snappy
import snappy
snappy.uncompress(snappy_data)

# zstd
import zstd
zstd.decompress(zstd_data)

# blosc
import blosc
blosc.decompress(blosc_data)

# lzma
import lzma
lzma.decompress(lzma_data)
