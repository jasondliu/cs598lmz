import bz2
# Test BZ2Decompressor

data = bz2.compress(b'The quick brown fox jumped over the lazy dog.')
print(data)

bz_decompressor = bz2.BZ2Decompressor()
print(bz_decompressor.decompress(data))

