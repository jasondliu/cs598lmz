import bz2
# Test BZ2Decompressor.inflate()
compressed = bz2.compress(b'Hello there')
decompressor = bz2.BZ2Decompressor()
