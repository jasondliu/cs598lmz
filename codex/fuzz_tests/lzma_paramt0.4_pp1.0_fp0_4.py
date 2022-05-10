from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用LZMA压缩
import lzma

data = b'Lots of data here'

with lzma.open('file.xz', 'wt') as f:
    f.write(data)

with lzma.open('file.xz', 'rt') as f:
    print(f.read())

# 压缩算法的选择
import bz2
import lzma
import zipfile

with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

with lzma.open('file.xz', 'wt') as f:
    f.write(data)

with zipfile.ZipFile('file.zip', 'w') as f:
    f.write('file.txt')

# 通过zlib进行数据压缩
import zlib

s = b'witch which has which witches wrist watch'

