import bz2
bz2.BZ2File('data/example.bz2')

import gzip
gzip.open('data/example.gz')

import lzma
lzma.open('data/example.xz')

# 其他的文件压缩格式，如ZIP，RAR，7z等等，可以使用第三方的包来读取。

# 如果你想把压缩文件读取到内存中去，可以使用io模块中的BytesIO()函数。

import bz2
with bz2.open('data/example.bz2', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('data/example.bz2', 'rt') as f:
    for line in
