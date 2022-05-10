from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x36\x31\x41\x59\x26\x53\x59')

# Decompress the entire file
open('sample.bz2', 'rb').read()

# Decompress the entire file
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Decompress an incomplete file
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Decompress the
