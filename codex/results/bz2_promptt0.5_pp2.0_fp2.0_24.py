import bz2
# Test BZ2Decompressor.
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY')

# Test BZ2Compressor.
compressor = bz2.BZ2Compressor()
compressor.compress(b'foo')

# Test round trip.
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(b'foo')
compressed += compressor.flush()
compressed

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# Test with a file.
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(b'foo')

with bz2.BZ2File('file.bz2', 'r') as f:
    f.read()

# Test with a file-like object.
with open('file.bz2', 'rb') as f:
    bz2.BZ2File(f,
