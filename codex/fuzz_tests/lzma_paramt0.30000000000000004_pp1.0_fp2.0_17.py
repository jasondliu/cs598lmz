from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress with lzma.decompress
import lzma
lzma.decompress(data)

# decompress with xz.decompress
import xz
xz.decompress(data)

# decompress with zlib.decompress
import zlib
zlib.decompress(data)
</code>

