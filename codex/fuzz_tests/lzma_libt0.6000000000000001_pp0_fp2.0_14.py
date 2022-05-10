import lzma
lzma.LZMACompressor().compress(b"Hello")

# compress data
import zlib
zlib.compress(b"Hello")

# decompress data
import zlib
zlib.decompress(b"x\x9cK\xcb\xcf\x07\r\x00\x02\x82\x01E")

# compress data
import bz2
bz2.compress(b"Hello")

# decompress data
import bz2
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# compress data
import lzma
lzma.compress(b"Hello")

# decompress data
import lzma
lzma.decompress(b'\xfd\x37\x7a\x58
