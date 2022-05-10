import bz2
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()

import lzma
lzma_file = lzma.LZMAFile('example.xz')
lzma_file.read()

# 12.2.2 将文本或二进制数据写入压缩文件
import gzip
with gzip.open('example.txt.gz', 'wt') as f:
    f.write(text)

with gzip.open('example.txt.gz', 'rt') as f:
    text = f.read()

with gzip.open('example.txt.gz', 'wt', compresslevel=5) as f:
    f.write(text)

with gzip.open('example.bin.gz', 'wb') as f:
    f.write(bin_data)

with gzip.open('example.bin.gz', 'rb') as f:
    bin_data = f.read
