import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
print('Input contains {} bytes'.format(len(b'El ni\xc3\xb1o come camar\xc3\xb3n, which is Spanish for "The boy eats shrimp".')))
compressed_data = compressor.compress(b'El ni\xc3\xb1o come camar\xc3\xb3n, which is Spanish for "The boy eats shrimp".')
trailer = compressor.flush()
print('Compressed data contains {} bytes'.format(len(compressed_data)))
print('Trailer contains {} bytes'.format(len(trailer)))
decompressor = lzma.LZMADecompressor()
uncompressed_data = decompressor.decompress(compressed_data + trailer)
print('Uncompressed data contains {} bytes'.format(len(uncompressed_data)))
