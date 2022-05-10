import bz2
# Test BZ2Decompressor and BZ2Compressor.

# Test compress() and decompress() with simple strings.
print(bz2.compress(b"hello"))
print(bz2.decompress(_))
# Test compress() and decompress() with binary data (compress level 9).
data = b"junk" * 1024
print(bz2.compress(data, 9))
compressed = _
print(bz2.decompress(compressed))
# Test BZ2Compressor.compress() and BZ2Decompressor.decompress()
# with binary data (compress level 1).

compressor = bz2.BZ2Compressor(1)
decompressor = bz2.BZ2Decompressor()

data = b"junk" * 1024
compressed = b""
decompressed = b""

compressed += compressor.compress(data)
compressed += compressor.flush()

decompressed += decompressor.decompress(compressed)

print(len(data))
print(len(compressed))
print(len
