from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

s = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
BZ2Decompressor().decompress(s)

# Python 3
import bz2
bz2.decompress(s)

# Python 2
import bz2
bz2.decompress(s)


s = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
BZ2Decompressor().decompress(s)


s = b'this is a test'
bz2.compress(s
