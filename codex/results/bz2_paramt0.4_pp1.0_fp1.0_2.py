from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(zlib.decompress(data)))

# bz2.decompress(zlib.decompress(data))
# zlib.decompress(bz2.decompress(data))

import zlib
import bz2
import sys

data = bz2.decompress(zlib.decompress(sys.stdin.buffer.read()))
sys.stdout.buffer.write(data)
