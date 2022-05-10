from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 读写压缩文件
# 读写bz2文件
import bz2
with bz2.open('somefile.bz2', 'wt', encoding='utf-8') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'rt', encoding='utf-8') as f:
    print(f.read())

# 读写gz文件
import gzip
with gzip.open('somefile.gz', 'wt', encoding='utf-8') as f:
    f.write(text)

with gzip.open('somefile.gz', 'rt', encoding='utf-8') as f:
    print(f.read())

# 在文件系统中查找文件
# 使用os.walk()
import os
os.chdir('/home/jack/python')
for root, dirs, files
