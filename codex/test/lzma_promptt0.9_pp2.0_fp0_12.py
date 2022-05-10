import lzma
# Test LZMADecompressor for read(0) function
#
# Any read(0) operation should return an empty bytes object.
#
dcomp = lzma.LZMADecompressor()
# test it with a new uncompressed stream
this_stream = dcomp.decompress(b'foo')
