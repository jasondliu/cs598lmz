import bz2
bz2.BZ2Compressor()

# A compressed file can be read like any other file:

with bz2.open(bz2_file, 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

# ### Gzip
# 
# * gzip is a format that uses the same algorithm as zip, but is tuned for compression only and always creates a single file.
# * The gzip format is typically used to compress just single files.
# * It is not a file archiver like zip or tar.

import gzip

# gzip.open() accepts the same arguments as the built-in open() function

with gzip.open(gz_file, 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

# ## The pickle module
# 
# * The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes.
# * This process is also called serializing — converting a data structure to a flat file.
# * Reconstruct
