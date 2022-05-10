from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

s = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
b = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
import bz2

# First try to decompress using bz2
print(bz2.decompress(s))

# If it fails, it's because it's compressed using the older algorithm,
# so use the compat module instead
print(bz2.decompress(b))

# If you want to determine which compression algorithm was used,
# you can try the decompress function and
