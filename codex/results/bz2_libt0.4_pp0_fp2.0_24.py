import bz2
bz2.decompress(compressed_data)

# bz2.compress()
# bz2.decompress()

# bz2.BZ2Compressor()
# bz2.BZ2Decompressor()

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World')
compressor.flush()

import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# zlib.compress()
# zlib.decompress()

# zlib.compressobj()
# zlib.decompressobj()

import zlib
compressor = zlib.compressobj(9)
compressor.compress(b'Hello World')
compressor.flush()

import zlib
decompressor = zlib.decompressobj()
decompressor.decompress(compressed_data)

# lzma.compress()
# lzma.decompress
