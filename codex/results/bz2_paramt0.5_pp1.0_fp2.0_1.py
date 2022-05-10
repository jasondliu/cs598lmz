from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 更一般的，可以使用任意的压缩器来操作二进制数据。
# zlib 模块可以为你提供通用的压缩和解压缩接口。下面是一个简单的例子：
import zlib

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

# 如果数据很小，压缩后反而会更大，这时就不建议使用压缩技术了。
