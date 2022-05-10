import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(filename)

# tar.gz
import tarfile
tarfile.open(filename, "r:gz")

# tar.bz2
import tarfile
tarfile.open(filename, "r:bz2")

# tar.xz
import tarfile
tarfile.open(filename, "r:xz")

# tar.lzma
import tarfile
tarfile.open(filename, "r:lzma")

# tar.lz
import tarfile
tarfile.open(filename, "r:lz")

# tar.Z
import tarfile
tarfile.open(filename, "r:Z")

# tar.lz4
import tarfile
tarfile.open(filename, "r:l
