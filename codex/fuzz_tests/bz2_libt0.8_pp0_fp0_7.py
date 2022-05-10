import bz2
bz2.BZ2File(f, 'w')

import os
os.system('tar -czf archive.tar.gz *')

import shutil
shutil.make_archive('archive', 'zip', root_dir=...)

###30.2.2 解压缩
import gzip
f = gzip.open('file.gz', 'rb')
f.read()
f.close()

import bz2
f = bz2.BZ2File('file.bz2', 'rb')
f.read()
f.close()

import zipfile
z = zipfile.ZipFile('example.zip')
z.extractall()
z.close()

import tarfile
tar = tarfile.open('example.tar.gz')
tar.extractall()
tar.close()

import shutil
shutil.unpack_archive('example.zip')


###30.3 流缓冲和字符编码
import gzip
f = gzip.open('
