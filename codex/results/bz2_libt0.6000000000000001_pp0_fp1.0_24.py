import bz2
bz2.decompress(bz2_data)

# bzip2 compression
bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress(lorem)
bz2_comp.flush()

# lzma compression
import lzma
lzma.decompress(lzma_data)

# lzma compression
lzma_comp = lzma.LZMACompressor()
lzma_comp.compress(lorem)
lzma_comp.flush()

# zlib compression
import zlib
zlib.decompress(zlib_data)

# zlib compression
zlib.compress(lorem)

# zlib decompression
import zlib
zlib.decompress(zlib_data)

# zlib compression
zlib.compress(lorem)



# ----------------------------------------------------------------------------------------------------------------------

# Sampling and shuffling

# Sampling
import random
import string

def process(filename, size):
    with open(filename) as f:
