from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 使用bz2.decompress()函数解压缩
import bz2
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# 使用bz2.BZ2Decompressor类解压缩
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
data = decompressor.decompress(b'BZh91AY&
