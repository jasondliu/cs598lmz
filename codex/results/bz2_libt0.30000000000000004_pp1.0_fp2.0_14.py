import bz2
bz2.decompress(bz2_data)

#-------------------------------------------------------------------------------
# bz2.compress(data, compresslevel=9)
#-------------------------------------------------------------------------------
# Compresses the data in data, returning a new string containing the compressed data.
# compresslevel, if given, must be a number between 1 and 9.

import bz2
bz2.compress(b'Hello World')

#-------------------------------------------------------------------------------
# bz2.BZ2Compressor(compresslevel=9)
#-------------------------------------------------------------------------------
# Return a compressor object, to be used for compressing data incrementally.
# compresslevel, if given, must be a number between 1 and 9.

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World')
compressor.flush()

#-------------------------------------------------------------------------------
# bz2.BZ2Decompressor()
#-------------------------------------------------------------------------------
# Return a decompressor object, to be used for decompressing data incrementally.

import bz2
decompressor = bz2.BZ2Decompressor()
decompressor
