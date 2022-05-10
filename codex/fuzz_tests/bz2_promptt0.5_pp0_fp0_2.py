import bz2
# Test BZ2Decompressor by feeding it the output of BZ2Compressor;
# this should produce the original input
c = bz2.BZ2Compressor()
d = bz2.BZ2Decompressor()

data = c.compress(b'1234567890') + c.flush()
print(data)

print(d.decompress(data))

data = c.compress(b'1234567890abcdefghij') + c.flush()
print(data)

print(d.decompress(data))

data = c.compress(b'1234567890abcdefghijklmnopqrstuvwxyz') + c.flush()
print(data)

print(d.decompress(data))

# Test BZ2Decompressor with multiple calls to decompress()
d = bz2.BZ2Decompressor()

data = c.compress(b'1234567890') + c.flush()
print(d.decompress(data))

data = c.compress(b'abcdefgh
