import bz2
# Test BZ2Decompressor's readline()

decompressor = bz2.BZ2Decompressor()

compressed = bz2.compress(b"this is a test\n" * 10)
data = decompressor.decompress(compressed)

decompressor = bz2.BZ2Decompressor()

