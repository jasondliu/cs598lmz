import bz2
# Test BZ2Decompressor

f = bz2.BZ2File('data/sample.bz2')
decompressor = bz2.BZ2Decompressor()

for chunk in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
    print(chunk)

f.close()

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

for data in ['a', 'b', 'c']:
    compressed = compressor.compress(data)
    print(compressed)

compressed = compressor.flush()
print(compressed)

# Test BZ2File

f = bz2.BZ2File('data/sample.bz2')
print(f.read())
f.close()

f = bz2.BZ2File('data/sample.bz2', 'r')
print(f.read())
f.close()

f = bz2.BZ2File('data/sample.bz2', 'w')

