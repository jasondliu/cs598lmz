import bz2
# Test BZ2Decompressor
s = bz2.BZ2Compressor().compress(b'hello world')
print(s)
bz2.BZ2Decompressor().decompress(s)
print(bz2.BZ2Decompressor().decompress(s))

# The maximum length of data to read in a single call to decompress().
# This limit prevents decompression bombs.
