from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'hello'

# 默认的压缩算法是 LZMA，也可以使用其他算法压缩
import bz2
bz2.compress(data)

# b'BZh91AY&SY\xea\x99\xc7\x0f\x00\x00\x00\x01\x01\x80\x00\x01\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

# 比如，bzip2 算法就比 LZMA 算法快，但是压缩比不如 LZMA 算法好

# 想要使用其他压缩算法，
