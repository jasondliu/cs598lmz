import bz2
# Test BZ2Decompressor

uncompressed_data = b'The same line, over and over.\n' * 10
compressed_data = bz2.compress(uncompressed_data)

print('Compressed is {} bytes; uncompressed is {} bytes'.format(
    len(compressed_data), len(uncompressed_data)))

decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)

print('Decompressed matches uncompressed: {}'.format(
    decompressed_data == uncompressed_data))

decompressed_data = b''
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: compressed_data, b''):
    decompressed_data += decompressor.decompress(chunk)

print('Decompressed matches uncompressed: {}'.format(
    decompressed_data == uncompressed_data))

# Test BZ2File

print('Writing to compressed file')
with bz2.open('uncompressed.txt.
