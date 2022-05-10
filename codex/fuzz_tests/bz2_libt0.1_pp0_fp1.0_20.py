import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果需要对大量的数据进行压缩，使用上述代码就很麻烦了，因为必须一次性将所有数据读取内存中。
# 如果数据量很大，内存就会不够用。
# 这种情况下，可以使用压缩文件对象，它在内存中创
