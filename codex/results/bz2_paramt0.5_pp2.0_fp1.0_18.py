from bz2 import BZ2Decompressor
BZ2Decompressor()

from bz2 import compress, decompress
compress(b'hello world!')
decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

import bz2
for line in bz2.open('example.bz2'):
    print(line)

import bz2
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

import bz2
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00
