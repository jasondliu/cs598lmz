from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 数据压缩
data = b'Lots of data here'
len(data)

import zlib
zlib.compress(data)

zlib.decompress(zlib.compress(data))

# 将数据压缩到一个文件中
import gzip
with gzip.open('somefile.gz', 'wb') as f:
    f.write(data)

with gzip.open('somefile.gz', 'rb') as f:
    print(f.read())

# 压缩和解压缩单个文件
import bz2
with bz2.open('somefile.bz2', 'wb') as f:
    f.write(data)

with bz2.open('somefile.bz2', 'rb') as f:
    print(f.read())

# 压缩和
