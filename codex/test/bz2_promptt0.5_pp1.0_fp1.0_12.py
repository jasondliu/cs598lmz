import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
data += bz2.compress(b"this is a test")

d = bz2.BZ2Decompressor()
print(d.decompress(data))
