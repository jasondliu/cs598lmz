from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzmaffi
from lzmaffi import decompress as lzma_decompress
lzma_decompress(data)

# zstandard
import zstandard as zstd
ctx = zstd.ZstdDecompressor()
ctx.decompress(data)

# zstandard-ctypes
import zstandard_ctypes as zstdct
ctx = zstdct.ZstdDecompressor()
ctx.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# blosc
import blosc
blosc.decompress(data)

# qlz
import qlz
qlz.decompress(data)

# snappy
import snappy
snappy.uncompress(data)

# zlib
import zlib
zlib.decompress(data, wbits=zlib.MAX_WBITS | 32)

# zopfli
import zopfli
zopfli.decompress(data
