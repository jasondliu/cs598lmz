import bz2
# Test BZ2Decompressor

data = bz2.compress(b'hello world')

d = bz2.BZ2Decompressor()
d.decompress(data)

