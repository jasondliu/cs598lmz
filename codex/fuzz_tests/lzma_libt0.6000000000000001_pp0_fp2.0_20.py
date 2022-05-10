import lzma
lzma.LZMADecompressor()

import bz2
bz2.BZ2Decompressor()

import zlib
zlib.decompressobj()

# 读取压缩文件
# 读取ZIP文件
import zipfile
with zipfile.ZipFile('example.zip') as zf:
    print(zf.namelist())
    with zf.open('README.txt') as f:
        print(f.read(100))

# 读取TAR文件
import tarfile
with tarfile.open('example.tar') as tf:
    print(tf.getnames())
    t = tf.extractall()
    print(t)

# 创建ZIP文件
import zipfile
import os
import shutil
shutil.make_archive('example', 'zip', root_dir='./')

# 创建TAR文件
import tarfile
with tarfile.
