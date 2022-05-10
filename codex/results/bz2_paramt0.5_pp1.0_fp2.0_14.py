from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data)) == data

# 使用自定义的压缩算法
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# 使用更高级的工具：压缩文件
# 压缩文件
import gzip
f = open('somefile.gz', 'wb')
with gzip.open(f, 'wt') as f2:
    f2.write(text)
# 解压文件
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# 使用bz2压缩文件
import bz2
f = open('somefile.bz2
