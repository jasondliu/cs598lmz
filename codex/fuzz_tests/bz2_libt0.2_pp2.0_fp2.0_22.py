import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 可以使用zipfile模块来读取zip文件
import zipfile
with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.txt'))
    print(zf.read('test.txt'))

# 可以使用tarfile模块来读取tar文件
import tarfile
with tarfile.open('test.tar', 'r') as tf:
    print(tf.getnames())
    print(tf.getmember('test.txt'))
    print(tf.extractfile('test.txt').read())


