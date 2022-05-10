import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

d = bz2.BZ2Decompressor()
print(d.decompress(data))
