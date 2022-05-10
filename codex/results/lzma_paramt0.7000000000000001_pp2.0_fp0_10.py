from lzma import LZMADecompressor
LZMADecompressor().decompress(compressedData)

from zlib import decompress
decompress(compressedData)

from bz2 import decompress
decompress(compressedData)

from snappy import decompress
decompress(compressedData)

from zstd import decompress
decompress(compressedData)

from brotli import decompress
decompress(compressedData)

from lz4 import block, frame
block.decompress(compressedData)
frame.decompress(compressedData)

from lz4.block import decompress as decompress_block
decompress_block(compressedData)
from lz4.frame import decompress as decompress_frame
decompress_frame(compressedData)

from lzma import decompress as decompress_lzma
decompress_lzma(compressedData)

from gzip import decompress as decompress_gzip
decompress_gzip(compressedData)

from bz2 import decompress as decompress_bz2
decompress
