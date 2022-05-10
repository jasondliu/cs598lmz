import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果需要对大量的数据进行压缩，最好使用压缩文件。
# 压缩文件的读写操作与普通文件一样，只是在打开文件时传入了一个参数。
# 压缩文件的内容是压缩后的数据，因此可以直接读取压缩文件的内容
