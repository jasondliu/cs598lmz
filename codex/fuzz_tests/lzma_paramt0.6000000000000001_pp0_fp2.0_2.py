from lzma import LZMADecompressor
LZMADecompressor.decompress(b'<lzma-data>')

# bz2
import bz2
bz2.decompress(b'<bz2-data>')

# gzip
import gzip
gzip.decompress(b'<gzip-data>')

# zip
import zipfile
with zipfile.ZipFile('<zip-file>') as zf:
    print(zf.read(zf.namelist()[0]))

# tar
import tarfile
with tarfile.open('<tar-file>') as tf:
    print(tf.extractfile(tf.getnames()[0]).read())
