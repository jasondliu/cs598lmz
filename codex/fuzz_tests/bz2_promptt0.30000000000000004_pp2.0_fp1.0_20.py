import bz2
# Test BZ2Decompressor
with bz2.open('sample.bz2') as f:
    print(f.read())

# Test BZ2Compressor
with bz2.open('sample.bz2', 'wt') as f:
    f.write('Hello World!')

# Test BZ2File
with bz2.open('sample.bz2', 'rt') as f:
    print(f.read())

# Test compress() and decompress()
compressed = bz2.compress(b'Hello World!')
print(compressed)
print(bz2.decompress(compressed))

# Test BZ2Compressor.compress() and BZ2Decompressor.decompress()
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(b'Hello World!')
compressed += compressor.flush()
print(compressed)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(compressed))

# Test BZ2File.read
