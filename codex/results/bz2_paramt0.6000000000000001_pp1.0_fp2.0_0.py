from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# zlib
from zlib import decompress
decompress(compressed_data)

# zip
from zipfile import ZipFile
z = ZipFile('readme.zip', 'r')
z.extractall()

# tar
from tarfile import TarFile
t = TarFile('readme.tar', 'r')
t.extractall()

# gzip
from gzip import GzipFile
g = GzipFile('readme.gz', 'r')
g.read()

# read from file
f = open('readme.bz2', 'rb')
decompressor = BZ2Decompressor()
for data in iter(lambda : f.read(100 * 1024), b''):
    rv = decompressor.decompress(data)
    if rv:
        print(rv)
f.close()

# compress data
from zlib import compress
compressed_data = compress(data)

# bz2
from bz2 import compress
compressed_data = compress(data
