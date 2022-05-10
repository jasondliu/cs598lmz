import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# tar
import tarfile
tarfile.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar.gz
import tarfile
import gzip
tarfile.open(filename, mode='r:gz')

# tar.bz2
import tarfile
import bz2
tarfile.open(filename, mode='r:bz2')

# tar.xz
import tarfile
import lzma
tarfile.open(filename, mode='r:xz')

# zip
import zipfile
zipfile.ZipFile(filename, mode='r')

# zip.gz
import zipfile
import gzip
zipfile.ZipFile(filename, mode='r')

# zip.bz2
import zipfile
import bz2
zipfile.ZipFile(filename, mode='r')

# zip
