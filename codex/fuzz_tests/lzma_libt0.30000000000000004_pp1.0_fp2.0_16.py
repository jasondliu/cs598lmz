import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 压缩和解压缩文件
import gzip
with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

with gzip.open('file.txt.gz', 'wt') as f:
    f.write(text)

# 压缩和解压缩文件
import bz2
with bz2.open('file.txt.bz2', 'rt') as f:
    text = f.read()

with bz2.open('file.txt.bz2', 'wt') as f:
    f.write(text)

# 压缩和解
