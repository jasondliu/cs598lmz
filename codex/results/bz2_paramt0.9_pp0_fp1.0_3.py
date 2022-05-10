from bz2 import BZ2Decompressor
BZ2Decompressor

# uncompressed_data = b"Lots of content here"
# Algorithm: http://en.wikipedia.org/wiki/Bzip2#Sample_implementation

print('-' * 10, 'bz2', '-' * 10)
compressor = BZ2Compressor()

compressor.compress(b"some data")
compressor.compress(b"some more data")

compressed_data = compressor.flush()

# print(compressed_data)

bz2_decompressor = BZ2Decompressor()
bz2_decompressor.decompress(compressed_data)

########################################################################################################################
# lzma
########################################################################################################################

from lzma import open as open_lzma
from lzma import LZMAFile

# Algorithm: http://www.7-zip.org/sdk.html

print('-' * 10, 'lzma', '-' * 10)
compressor = LZMACompressor()

compressor.compress(b"some data")
compressor.comp
