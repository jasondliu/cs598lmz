import bz2
bz2_file = bz2.BZ2File('data/file.bz2')
data = bz2_file.read()
bz2_file.close()

# gzip
import gzip
gzip_file = gzip.open('data/file.gz', 'rt')
data = gzip_file.read()
gzip_file.close()

# lzma
import lzma
lzma_file = lzma.open('data/file.xz')
data = lzma_file.read()
lzma_file.close()

# tar
import tarfile
tar = tarfile.open('data/file.tar.gz')
tar.extractall()
tar.close()

# zip
import zipfile
zip = zipfile.ZipFile('data/file.zip')
zip.extractall()
zip.close()
