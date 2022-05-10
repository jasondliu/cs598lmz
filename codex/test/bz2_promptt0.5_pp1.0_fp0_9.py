import bz2
# Test BZ2Decompressor on an empty file
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(b'')

# Test BZ2Decompressor on a file with no compressed data
