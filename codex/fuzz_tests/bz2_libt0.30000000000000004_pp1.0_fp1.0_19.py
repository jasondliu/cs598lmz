import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import gzip
gzip.compress(b'Hello World!')

import zlib
zlib.compress(b'Hello World!')
zlib.decompress(zlib.compress(b'Hello World!'))

# 如果要压缩的数据很小，就不要使用压缩模块。因为压缩后的数据反而更大。

# 压缩文件
import gzip
with gzip.open('somefile.gz', 'wb') as f:
    f.write(b'Hello World!')

# 读取压缩文件
with gzip.open('somefile.gz', 'rb') as f:
    f.read()

# 压缩文件的名称
