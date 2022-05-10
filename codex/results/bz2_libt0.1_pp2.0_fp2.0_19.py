import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 在压缩数据的时候，有时候你可能仅仅只是想得到一个校验码，以验证数据完整性。如果是这样的话，你可以使用
# hashlib 模块中的一些恒等哈希函数。比如，下面是计算一个 SHA1 校验码的例子：
import
