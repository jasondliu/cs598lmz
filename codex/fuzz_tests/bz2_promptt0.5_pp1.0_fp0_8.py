import bz2
# Test BZ2Decompressor.decompress() with a large input
# and a large output buffer.

data = bz2.BZ2Compressor().compress(b"a" * 2048)

decompressor = bz2.BZ2Decompressor()

result = decompressor.decompress(data, 1024 * 1024)

print(len(result))

# Test BZ2Decompressor.decompress() with a large input
# and a small output buffer.

data = bz2.BZ2Compressor().compress(b"a" * 2048)

decompressor = bz2.BZ2Decompressor()

result = decompressor.decompress(data, 1)

print(len(result))
