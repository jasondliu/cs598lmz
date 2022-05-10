import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 可以使用shutil模块的make_archive()和unpack_archive()函数分别打包和解包文件
import shutil
shutil.make_archive('example', 'zip', root_dir='.')
shutil.unpack_archive('example.zip', 'example', 'zip')

# 对于更底层的操作，可以使用tarfile模块
import tarfile
with tarfile.open('example.tar', 'w') as tr:
    tr.add('example')

with tarfile.open('example.tar', 'r') as tr:
