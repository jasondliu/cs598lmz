from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

import struct
header = struct.unpack('<Q',compressed[:8])
header

original_size = header[0]
original_size

TAG3 = compressed[8:10]
TAG3

uncompressed = LZMADecompressor().decompress(compressed[10:])
len(uncompressed)

uncompressed == data
