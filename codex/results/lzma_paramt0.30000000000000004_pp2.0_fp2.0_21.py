from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = bz2.compress(original_data)
bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
zlib.decompress(compressed_data)

# gzip
import gzip
compressed_data = gzip.compress(original_data)
gzip.decompress(compressed_data)

# zipfile
import zipfile
with zipfile.ZipFile('my_file.zip', 'w') as zf:
    zf.write('my_file.txt')

with zipfile.ZipFile('my_file.zip', 'r') as zf:
    zf.extractall()

# tarfile
import tarfile
with tarfile.open('my_file.tar.gz', 'w:gz') as tf:
    tf.add('my_file.txt')

with tarfile.open('my_
