from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ)

import zlib
d= zlib.decompressobj(16+zlib.MAX_WBITS)
print d.decompress(data)
