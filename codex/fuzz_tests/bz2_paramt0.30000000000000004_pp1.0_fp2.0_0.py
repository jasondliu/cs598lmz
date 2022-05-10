from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用bz2模块的BZ2Decompressor类来构造一个解压器对象，然后使用decompress()方法来解压数据
# 这个类的使用方式和zlib模块类似，只是它不支持压缩级别的设置
# 使用BZ2Decompressor类可以很方便的解压缩文件，比如：

import os
import bz2

uncompressed_data = b''
with bz2.BZ2File('example.bz2', 'rb') as input:
    for data in iter(lambda: input.
