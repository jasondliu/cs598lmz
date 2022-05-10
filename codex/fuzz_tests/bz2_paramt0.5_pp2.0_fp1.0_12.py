from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.decompress()
bz2.decompress(bz2_data)

# lzma.decompress()
lzma.decompress(lzma_data)

# zlib.decompress()
zlib.decompress(zlib_data)

# zlib.decompressobj()
zlib.decompressobj().decompress(zlib_data)

# zlib.decompressobj()
zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(zlib_data)

# zlib.decompressobj()
zlib.decompressobj(zlib.DEFLATED, zlib.MAX_WBITS | 16).decompress(zlib_data)

# zlib.decompressobj()
zlib.decompressobj(zlib.DEFLATED).decompress(zlib_data)

# zlib.decompressobj()
zlib.decompresso
