import bz2
bz2.decompress(data)

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# zlib
import zlib
zlib.compress(data)
zlib.decompress(data)

# zlib.compressobj
# zlib.decompressobj

# lzma
import lzma
lzma.compress(data)
lzma.decompress(data)

# lzma.LZMACompressor
# lzma.LZMADecompressor

# lzma.open
# lzma.open(filename, mode='rb', format=None, check=-1, preset=None, filters=None)

# lzma.FILTER_LZMA1
# lzma.FILTER_LZMA2
# lzma.FILTER_DELTA
# lzma.FILTER_X86
# lzma.FILTER_IA64
# lzma.FILTER_ARM
# lzma.FILTER_ARMTHUM
