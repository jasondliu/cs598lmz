from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Using bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Using zlib
import zlib
zlib.decompress(data)
