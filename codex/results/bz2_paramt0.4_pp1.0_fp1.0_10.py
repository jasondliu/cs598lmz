from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")

# 使用bz2.decompress()解压缩
import bz2
un = bz2.decompress(b"BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
print(un)

# 关于bz2.decompress()的注意事项
# 如果解压缩的数据不是由bz2.compress()方法压缩的，
#
