import bz2
bz2.BZ2File('file.bz2')

# open a gzip file
import gzip
gzip.open('file.gz')

# open a lzma file
import lzma
lzma.open('file.xz')

# open a tar file
import tarfile
tar = tarfile.open('file.tar')

# open a zip file
import zipfile
zip = zipfile.open('file.zip')

# open a Z file
import Z
z = Z.open('file.z')
