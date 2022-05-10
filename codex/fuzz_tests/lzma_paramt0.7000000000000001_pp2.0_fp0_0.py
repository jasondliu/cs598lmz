from lzma import LZMADecompressor
LZMADecompressor().decompress(raw_data)

# See [1]_ for a more complete list of available compression functions.

###############################################################################
# Utilities
# ---------
#
# The :mod:`gzip` module provides a simple interface to compress and decompress
# files, but its not clear how to transfer the compressed data over the network.
# The :mod:`gzip` module provides the ``GzipFile`` class which is modeled after
# Python’s ``File Object``. This class reads and writes gzip-format files,
# automatically compressing or decompressing the data so that it looks like an
# ordinary file object.
#
# For example, to write compressed data to a buffer:

import io
import gzip
buf = io.BytesIO()
with gzip.GzipFile(mode='wb', fileobj=buf, compresslevel=9) as f:
    f.write(b'Hello Python!')

# To read a compressed file:
buf.seek(0)
with gzip.GzipFile(mode='rb', fileobj=buf) as f:
    print
