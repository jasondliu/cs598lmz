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

