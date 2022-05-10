from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# #############################################################################
# Gzip and Gunzip
# #############################################################################
# gzip and gunzip are very common in the wild, but they are really not
# meant for random access. So, you should use gzip only if you need to
# save space.
import gzip
s = b'witch which has which witches wrist watch'
len(s)

# Compress the data
t = gzip.compress(s)
len(t)

# Decompress the data
gzip.decompress(t)

# Write compressed data to a file
with gzip.open('somefile.gz', 'wt') as f:
    f.write('Contents of the file go here.')

# Read back the compressed data
with gzip.open('somefile.gz', 'rt') as f:
    file_content = f.read()

# #############################################################################
# Reading and Writing ZIP Archives
# #############################################################################
# The zipfile module gives you a way of compress data that is
# compatible
