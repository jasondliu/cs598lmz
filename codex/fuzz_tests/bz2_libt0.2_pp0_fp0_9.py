import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 对于大型的数据压缩，最好使用压缩文件。
# 压缩文件的读写操作都是通过open()函数打开后返回的文件对象进行的。
# 压缩文件的写入操作通过write()方法，压缩文件的读取操作通过read()方法。
# 压缩文件的关闭操作通
