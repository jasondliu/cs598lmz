import bz2
# Test BZ2Decompressor with EOFError exceptions.

data = open("/etc/services", "rb").read()
d = bz2.BZ2Decompressor()
print(repr(d.decompress(data)))
print(repr(d.decompress(data, 1)))
print(repr(d.decompress(data, 2)))
