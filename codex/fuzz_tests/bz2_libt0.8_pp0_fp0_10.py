import bz2
bz2_compression_data = bz2.compress(text_data)
print(bz2_compression_data)

import zlib
zlib_compression_data = zlib.compress(text_data)
print(zlib_compression_data)

import lzma
lzma_compression_data = lzma.compress(text_data)
print(lzma_compression_data)
