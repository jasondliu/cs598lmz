from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Using the bz2 module
import bz2
bz2.decompress(bz2_data)

# Using the lzma module
import lzma
lzma.decompress(lzma_data)

# Using the zlib module
import zlib
zlib.decompress(zlib_data)

# Using the gzip module
import gzip
gzip.decompress(gzip_data)

# Using the zipfile module
from zipfile import ZipFile
with ZipFile('example.zip') as zf:
    zf.extractall()

# Using the tarfile module
from tarfile import TarFile
with TarFile('example.tar.gz') as tf:
    tf.extractall()

# Using the tarfile module
from tarfile import TarFile
with TarFile('example.tar.bz2') as tf:
    tf.extractall()

# Using the tarfile module
from tarfile import TarFile
with TarFile('example.tar.
