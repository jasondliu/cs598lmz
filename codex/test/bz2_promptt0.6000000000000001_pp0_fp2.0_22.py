import bz2
# Test BZ2Decompressor

data = bz2.compress(b'*' * 100)

print(len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

