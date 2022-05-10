from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_bytes)

LZMADecompressor().decompress(lzma_bytes).decode()

import zlib
zlib.decompress(zlib_bytes)

zlib.decompress(zlib_bytes).decode()
