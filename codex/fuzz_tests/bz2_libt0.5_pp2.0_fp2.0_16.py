import bz2
bz2.BZ2File(filename)

# open a gzip compressed file
import gzip
gzip.open(filename, mode='rb')

# open a bzip2 compressed file
import bz2
bz2.open(filename, mode='wt')

# open a lzma compressed file
import lzma
lzma.open(filename, mode='wt')

# open a zip file
import zipfile
zf = zipfile.ZipFile(filename)

# read zip file
zf.read('README.txt')

# write zip file
zf = zipfile.ZipFile(filename, mode='w')
zf.write(filename)
zf.close()

# read text from a gzip compressed file
import gzip
with gzip.open(filename, 'rt') as f:
    text = f.read()

# write compressed data to a gzip file
import gzip
with gzip.open(filename, 'wt') as f:
    f.write(text)

# read compressed data from a gzip file
import g
