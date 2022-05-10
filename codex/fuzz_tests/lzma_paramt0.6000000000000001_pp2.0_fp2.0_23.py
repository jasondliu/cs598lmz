from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#compress
import zlib
zlib.compress(data)

#decompress
import zlib
zlib.decompress(data)

#compress
import bz2
bz2.compress(data)

#decompress
import bz2
bz2.decompress(data)

#compress
import lzma
lzma.compress(data)

#decompress
import lzma
lzma.decompress(data)
