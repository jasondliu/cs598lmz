import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SY.  \x00\x00\x00\x01\x80\x02$\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

decompressor = bz2.BZ2Decompressor()
