import lzma
lzma.LZMACompressor(preset=9)

from lzma import LZMAFile

with LZMAFile('foo.xz', 'w') as f:
    f.write(b'hello world')

with LZMAFile('foo.xz', 'r') as f:
    print(f.read())

# b'hello world'

with LZMAFile('foo.xz', 'r') as f:
    print(f.readline())

# b'hello world'

with LZMAFile('foo.xz', 'r') as f:
    print(f.readlines())

# [b'hello world']


# 读取压缩文件

import gzip

with gzip.open('foo.gz', 'rb') as f:
    file_content = f.read()

import bz2

with bz2.open('foo.bz2', 'rb') as f:
    file_content = f.read()

import lzma
