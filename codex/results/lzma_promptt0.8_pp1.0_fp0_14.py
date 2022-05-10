import lzma
# Test LZMADecompressor with a one-byte-long input stream.
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(b'\x00')
except EOFError as e:
    print(e)

# Test native LZMA compression and decompression.
# The input data will be compressed, converted to base64, then uncompressed.
s = b'The quick brown fox jumps over the lazy dog.'
print('Input:', s)
t = lzma.compress(s)
print('Compressed:', len(t), 'bytes')
print('Uncompressed:', len(lzma.decompress(t)), 'bytes')
print('Compressed and base64 encoded:', t.encode('base64'))

# Test the convenience functions.
compressed_data = lzma.compress(s)
print('Compressed:', len(compressed_data), 'bytes')
decompressed_data = lzma.decompress(compressed_data)
print('Uncompressed:', len(decompressed_
