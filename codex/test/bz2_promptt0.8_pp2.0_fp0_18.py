import bz2
# Test BZ2Decompressor
bz2c = bz2.BZ2Compressor(9)
bz2c.compress(b'hello world')

