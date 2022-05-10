from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\x00\x00\x00\x00')

# 6.3.3
# The bz2 module provides the BZ2Decompressor class, which acts as a binary file object and contains
# the following methods:
# • bz2.BZ2Decompressor.decompress(data, size)
# Decompresses size bytes of data. If size is omitted or None, it reads all bytes until the end of file
# (EOF) is reached. New in version 3.4.
# • bz2.BZ2Decompressor.__getstate__()
# Returns a tuple containing the state of the decompressor object.
# • bz2.BZ2Decompressor.__setstate__(state)
# Resets the decompressor to the state captured by state, which must be a tuple produced by
# __getstate__(). This method supports the unpickling protocol. New in version 3.4.
# • bz2.BZ2Decompressor.unused_data
# A bytes object containing any unused data from the end of
