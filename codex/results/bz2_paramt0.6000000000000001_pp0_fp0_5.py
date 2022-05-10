from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(d)

# bz2
# bz2.BZ2Compressor(...)
# bz2.BZ2Decompressor(...)

# zlib
from zlib import compress, decompress
d = compress(data)
data = decompress(d)

# zlib
# zlib.compress(...)
# zlib.decompress(...)

# zipfile
from zipfile import ZipFile, ZIP_DEFLATED
with ZipFile('test.zip', 'w', ZIP_DEFLATED) as f:
    f.write('test.txt')

# zipfile
# zipfile.ZipFile(...)
# zipfile.ZIP_DEFLATED

# tarfile
from tarfile import TarFile, open, TAR_GZIPPED
with TarFile.open('test.tar.gz', 'w:gz') as f:
    f.add('test.txt')

# tarfile
# tarfile.TarFile(...)
# tarfile.open(...)
# tarfile.TAR_GZIPPED


