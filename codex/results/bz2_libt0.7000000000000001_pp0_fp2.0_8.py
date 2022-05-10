import bz2
bz2.decompress(bz2_compressed)

# using lzma algorithm
import lzma
lzma_compressed = lzma.compress(sample_bytes)
lzma.decompress(lzma_compressed)

# using bz2 algorithm
import bz2
bz2_compressed = bz2.compress(sample_bytes)
bz2.decompress(bz2_compressed)

# using zlib algorithm
import zlib
zlib_compressed = zlib.compress(sample_bytes)
zlib.decompress(zlib_compressed)
