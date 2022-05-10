from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 'Beautiful is better than ugly.\n'

## 压缩

from bz2 import BZ2Compressor
compressor = BZ2Compressor()
print(compressor.compress(b'Beautiful is better than ugly.\n'))
print(compressor.flush())
