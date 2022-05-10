from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
                             b'\x6f\x6d\x69\x73\x6f\x3d\x33\x37\x37\x39'
                             b'\x37\x0a')

#-------------------------------------------------------------------------------

from bz2 import BZ2Decompressor
compressor = BZ2Decompressor()
next(compressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00'
                            b'\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91'
                            b'\xf08'))

#-------------------------------------------------------------------------------

from bz2 import BZ2Decompressor
compressor = BZ2Decompressor()
data = b'BZh91AY&SY\
