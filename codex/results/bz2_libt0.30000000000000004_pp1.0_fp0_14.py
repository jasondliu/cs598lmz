import bz2
bz2.decompress(data)

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'i am a string')
compressor.flush()

import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
decompressor.decompress(b'\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')
decompressor.flush()

# zlib
import zlib
s = b'witch which has which witches wrist watch'
len(s)

