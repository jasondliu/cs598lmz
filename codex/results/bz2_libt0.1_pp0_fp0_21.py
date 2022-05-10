import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

# 小结
# 在 Python 中，字符串是 str 类型，在内存中以 Unicode 表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把 str 变为以字节为单位的 bytes。
# Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示：x = b
