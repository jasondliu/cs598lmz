import bz2
# Test BZ2Decompressor

data = open('lorem.txt', 'rb').read()

compressor = bz2.BZ2Compressor()

compressed = compressor.compress(data)

compressed += compressor.flush()

# assert len(data) > len(compressed)

decompressor = bz2.BZ2Decompressor()

print('Decompressed: {!r}'.format(decompressor.decompress(compressed)))
print('Residual: {!r}'.format(decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()

print('Decompressed: {!r}'.format(decompressor.decompress(compressed)))
print('Residual: {!r}'.format(decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()

print('Decompressed: {!r}'.format(decompressor.decompress(compressed + b'hello')))
print('Residual: {!r
