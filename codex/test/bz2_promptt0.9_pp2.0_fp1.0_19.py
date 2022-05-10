import bz2
# Test BZ2Decompressor on small string.
s = bz2.decompress(bz2.compress(b'the quick brown fox'))
s

# Test on small file.
with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(b'honey')

with bz2.BZ2File('test.bz2', 'rb') as f:
    print(f.read())

# Incremental decompression.
b1 = bz2.BZ2Compressor().compress(bytes(range(10)))
b2 = bz2.BZ2Compressor().compress(bytes(range(10, 20)))
b3 = bz2.BZ2Compressor().compress(bytes(range(20, 30)))
d = bz2.BZ2Decompressor()
print(d.decompress(b1))
print(d.decompress(b2))
print(d.decompress(b3))
