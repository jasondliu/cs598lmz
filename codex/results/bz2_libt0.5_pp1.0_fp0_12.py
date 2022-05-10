import bz2
bz2.decompress(data)

# bzip2 compression is only available if the bz2 module is installed.
# The bz2 module provides a comprehensive interface for the bzip2 compression library.
# It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

# https://docs.python.org/3/library/bz2.html

# 1.2.2.2 gzip

import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

# The gzip module provides a file-like interface to GNU zip files, using zlib to compress and uncompress the data.

# https://docs.python.org/3/library/gzip.html

# 1.2.2.3 lzma

import lzma
s = b'witch which has which witches wrist watch'
len(s)

t = lzma.compress(s)

