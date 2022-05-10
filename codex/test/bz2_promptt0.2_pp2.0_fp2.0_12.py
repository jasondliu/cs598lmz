import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

