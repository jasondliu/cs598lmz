from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# b"YELLOW SUBMARINE"

# You can use this online tool to generate the compressed data
# http://www.txtwizard.net/compression

# https://docs.python.org/3/library/bz2.html

# https://docs.python.org/3/library/zlib.html

import zlib

print(zlib.decompress(b'x\x9cK\xca\xc9\xcf\xcb,\xcdM\xce\xcf\xca\xccK,I\xcd\xcf\xcc\xcbK\xccM\xce\xca\xcf\xcc\xcd\xce\xcf\xc9,*\xcc
