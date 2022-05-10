import bz2
# Test BZ2Decompressor.decompress() that returns less than
# the requested amount
co = bz2.BZ2Compressor(9)
t = co.compress(b'x' * 1000)
