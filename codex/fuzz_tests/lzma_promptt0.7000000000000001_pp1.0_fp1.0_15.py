import lzma
# Test LZMADecompressor
# with open('test-data/lzma/lzma.1', 'rb') as f:
#     data = lzma.LZMADecompressor().decompress(f.read())
#     print(data)

import bz2
# Test BZ2Decompressor
# with open('test-data/bzip2/bzip2.1', 'rb') as f:
#     data = bz2.BZ2Decompressor().decompress(f.read())
#     print(data)

from lzma import LZMAError
from bz2 import BZ2File, BZ2Compressor, BZ2Decompressor

# def decompress_file(compressed_file, decompressed_file):
#     LZMA_HEADER_MAGIC = bytearray([0xFD, 0x37, 0x7A, 0x58, 0x5A, 0x00])
#     BZIP2_HEADER_MAGIC = bytearray([0x42, 0x5A, 0x68
