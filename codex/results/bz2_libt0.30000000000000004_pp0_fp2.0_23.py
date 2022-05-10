import bz2
bz2.BZ2File('data/sample.bz2').read()

# gzip
import gzip
gzip.GzipFile('data/sample.gz').read()

# lzma
import lzma
lzma.LZMAFile('data/sample.xz').read()

# zip
import zipfile
zipfile.ZipFile('data/sample.zip').read('sample.txt')

# tar
import tarfile
tarfile.TarFile('data/sample.tar').read('sample.txt')

# tar.gz
import tarfile
tarfile.TarFile('data/sample.tar.gz').read('sample.txt')

# tar.bz2
import tarfile
tarfile.TarFile('data/sample.tar.bz2').read('sample.txt')

# tar.xz
import tarfile
tarfile.TarFile('data/sample.tar.xz').read('sample.txt')

# tar.lzma
import tarfile
tarfile.TarFile('data/sample.tar.lzma').read('
