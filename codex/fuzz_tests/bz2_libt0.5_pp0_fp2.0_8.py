import bz2
bz2.BZ2File('data/sample.json.bz2')

# gzip
import gzip
gzip.GzipFile('data/sample.json.gz')

# lzma
import lzma
lzma.LZMAFile('data/sample.json.xz')

# zip
import zipfile
z = zipfile.ZipFile('data/sample.zip')
z.extractall('data/sample')

# tar
import tarfile
t = tarfile.TarFile('data/sample.tar')
t.extractall('data/sample')

# tar.gz
import tarfile
t = tarfile.TarFile('data/sample.tar.gz')
t.extractall('data/sample')

# tar.bz2
import tarfile
t = tarfile.TarFile('data/sample.tar.bz2')
t.extractall('data/sample')

# tar.xz
import tarfile
t = tarfile.TarFile('data/sample.tar.xz')
t.extractall('
