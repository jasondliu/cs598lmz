import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(compressed)
with bz2.BZ2File('file.bz2', 'rb') as f:
    data = f.read()
assert data == uncompressed

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(uncompressed)
compressor.flush()
compressed = compressor.compress(uncompressed)
compressor.flush()
compressed += compressor.compress(uncompressed)
compressor.flush()
compressed += compressor.compress(uncompressed)
compressor.flush()
compressed += compressor.compress(uncompressed)
compressor.flush()
compressed += compressor.compress(uncompressed)
compressor.flush()
compressed += compressor.compress(uncompressed)
compressor
