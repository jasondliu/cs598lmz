import bz2
bz2.BZ2File('data/sample.bz2')

import gzip
gzip.open('data/sample.gz')

import lzma
lzma.LZMAFile('data/sample.xz')

# 使用zipfile
import zipfile
with zipfile.ZipFile('data/sample.zip') as zf:
    print(zf.namelist())
    print(zf.getinfo('sample.txt'))
    print(zf.getinfo('sample.txt').file_size)
    print(zf.getinfo('sample.txt').compress_size)
    print(zf.read('sample.txt'))
    with zf.open('sample.txt') as f:
        print(f.read())

# 创建zip文件
with zipfile.ZipFile('data/sample2.zip', 'w') as zf:
    zf.write('data/sample.txt')

# 创建压缩文件
with zipfile
