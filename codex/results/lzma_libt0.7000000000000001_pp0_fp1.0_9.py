import lzma
lzma.LZMACompressor(dict_size, check=0, preset=None)
lzma.LZMADecompressor(dict_size=2 ** 16, memlimit=None, filters=None)

import lzma
import os

# Initialize a compressor.  These are the default values:
compressor = lzma.LZMACompressor()

# You can then feed data to the compressor object using its compress()
# method.
with open('test.txt', 'rb') as fpin:
    with open('test.xz', 'wb') as fpout:
        fpout.write(compressor.compress(fpin.read()))

# Calling flush() gives us the remaining data compressed in the internal
# buffers.  It also resets the compressor object so that we may
# compress another file.
fpout.write(compressor.flush())

# Initialize a decompressor.  You may either specify a preset value, or
# pass a custom filter chain as a list of dicts.
decompressor = lzma.LZMAD
