import bz2
# Test BZ2Decompressor with an empty file
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'')

# Test BZ2Decompressor with a short file
decompressor = bz2.BZ2Decompressor()
