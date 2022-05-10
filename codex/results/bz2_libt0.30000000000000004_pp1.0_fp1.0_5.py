import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, 'rt')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zf = zipfile.ZipFile(filename)
zf.open(zf.infolist()[0])

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.extractfile(tf.getmembers()[0])

# filecmp
import filecmp
filecmp.cmp(src, dst, shallow=False)

# shutil
import shutil
shutil.copyfile(src, dst)
shutil.move(src, dst)

# glob
import glob
glob.glob('*.py')

# fnmatch
import fnmatch
fnmatch.fnmatch('foo.txt', '*.txt')
fnmatch.fnmatchcase('foo.txt', '*.TXT')

# os.path
import os.path
path = '/path/to/file.txt'
os
