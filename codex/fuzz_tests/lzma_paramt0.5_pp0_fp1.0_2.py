from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

import bz2
bz2.decompress(data)

import zlib
zlib.decompress(data)

# 以上的压缩和解压缩操作都需要创建一个压缩或解压缩的对象，然后一步一步调用它们的方法。
# 如果你只是简单的压缩和解压缩，那么可以使用 shutil 模块中提供的简单的压缩接口函数
import shutil
with open('somefile.gz', 'rb') as f_in:
    with gzip.open(f_in, 'rb') as f_out
