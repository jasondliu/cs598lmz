import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: f.read(100 * 1024), b''):
    decompressed += decompressor.decompress(chunk)
decompressed += decompressor.flush()

# Test BZ2File
f = bz2.BZ2File('file.bz2', 'rb')
decompressed = f.read()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
for chunk in iter(lambda: f.read(100 * 1024), b''):
    compressed += compressor.compress(chunk)
compressed += compressor.flush()

# Test BZ2File
f = bz2.BZ2File('file.bz2', 'wb')
f.write(compressed)
f.close()

# Test BZ2File
f = bz2.BZ2File('file.bz2', 'rb')
f.read()
f.close()

# Test BZ2File
f = bz2.
