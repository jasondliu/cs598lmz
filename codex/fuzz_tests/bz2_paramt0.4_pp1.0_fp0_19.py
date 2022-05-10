from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world'))

# bz2.BZ2Decompressor.decompress(data)
# bz2.BZ2Decompressor.flush()

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)

# ------------------------------------------------------------------------------
# lzma
# ------------------------------------------------------------------------------

import lzma
lzma.compress(b'hello world')
lzma.decompress(lzma.compress(b'hello world'))

# lzma.LZMACompressor.compress(data)
# lzma.LZMACompressor.flush()
# lzma.LZMADecompressor.decompress(data)
# lzma.LZMADecompressor.flush()

# lzma.compress(data, format=lzma.FORMAT_XZ, check=-1, preset=None, filters=None)
# lzma.decompress(data, format=l
