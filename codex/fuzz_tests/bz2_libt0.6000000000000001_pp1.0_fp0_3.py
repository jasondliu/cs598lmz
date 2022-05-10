import bz2
bz2.decompress(compressed_data)

compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# To read and write gzip-compressed files, the gzip module provides a very
# simple interface. The GzipFile class reads and writes gzip-format files,
# automatically compressing or decompressing the data so that it looks like
# any other file object.
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'rb') as f:
    data = f.read()

# The bz2 and lzma modules provide functions for compression as well as
# compression objects.
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with bz2.open('somefile
