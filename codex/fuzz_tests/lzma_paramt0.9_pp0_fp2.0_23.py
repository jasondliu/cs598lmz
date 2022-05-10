from lzma import LZMADecompressor
LZMADecompressor().decompress(LZMA_COMPRESSED)

import lzma
lzc = lzma.LZMACompressor()
f = lzc.compress(
    b'The quick brown fox jumps over the lazy dog.')
f += lzc.flush()
lzd = lzma.LZMADecompressor()
lzd.decompress(f)
