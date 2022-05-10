import bz2
# Test BZ2Decompressor
s = bz2.BZ2Compressor().compress(b'hello world')
print(s)
bz2.BZ2Decompressor().decompress(s)
print(bz2.BZ2Decompressor().decompress(s))

# The maximum length of data to read in a single call to decompress().
# This limit prevents decompression bombs.
print(bz2.decompress(s, limit=1))
print(bz2.decompress(s, limit=10))
print(bz2.decompress(s, limit=100))

# The compresslevel parameter, if given, must be a number between 1 and 9.
bz2.compress(b'hello world', compresslevel=9)
