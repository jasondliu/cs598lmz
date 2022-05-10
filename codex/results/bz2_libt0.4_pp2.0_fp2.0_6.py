import bz2
bz2.BZ2File('example.bz2')

# gzip
import gzip
gzip.open('example.gz')

# lzma
import lzma
lzma.LZMAFile('example.xz')

# zip
import zipfile
zipfile.ZipFile('example.zip')

# tar
import tarfile
tarfile.open('example.tar.gz')
tarfile.open('example.tar.bz2')

# Compressed files in the wild

# Reading from a Gzip file
with gzip.open('example.gz', 'rt') as f:
    text = f.read()

# Writing to a Gzip file
with gzip.open('example.gz', 'wt') as f:
    f.write(text)

# Reading from a BZIP2 file
with bz2.open('example.bz2', 'rt') as f:
    text = f.read()

# Writing to a BZIP2 file
with bz2.open('example.bz2', 'wt') as
